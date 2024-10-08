"""
Module inits FastAPI
"""

import os
from fastapi import FastAPI, UploadFile, File, status
from fastapi.responses import FileResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from pdf2image import convert_from_bytes
import google.generativeai as genai
from dotenv import load_dotenv
from app.constants import RESUME_REVIEW_PROMPT, JSON_RESPONSE_EXPECTED

load_dotenv()
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["Content-Disposition"],
)


@app.post("/api/resume-form/")
async def submit_resume(pdf_file: UploadFile = File(...)):
    """
    Takes in the submitted resume for review
    """
    try:
        pdfcontents = await pdf_file.read()
        img = convert_from_bytes(
            pdfcontents, output_folder="./temp/", fmt="png", dpi=200
        )

        filename = img[0].filename

        headers = {"Content-Disposition": filename}

        return FileResponse(filename, filename=filename, headers=headers)
    except FileNotFoundError:
        return {
            "message": "File not found: " + filename,
            "code": status.HTTP_404_NOT_FOUND,
        }
    except ValueError as e:
        return {
            "message": "Error processing PDF: " + str(e),
            "code": status.HTTP_400_BAD_REQUEST,
        }
    except IndexError:
        return {
            "message": "No pages found in the PDF document.",
            "code": status.HTTP_400_BAD_REQUEST,
        }
    except OSError as e:
        return {
            "message": "File system error: " + str(e),
            "code": status.HTTP_500_INTERNAL_SERVER_ERROR,
        }
    except BaseException as e:
        print(f"An unexpected error occurred: {e}")
        raise


class ReviewRequest(BaseModel):
    """
    Testing
    """

    file_name: str | None = ""
    job_description: str | None = ""


@app.post("/api/remove-file/")
def remove_resume_file(req: ReviewRequest):
    """
    Received the name of the file to be removed
    """
    if not req.file_name:
        return JSONResponse({"msg": "Error in File name"}, status_code=404)

    try:
        os.remove(req.file_name)
    except FileNotFoundError as e:
        return JSONResponse({"msg": "File not found: " + str(e)}, status_code=404)

    return JSONResponse(
        {"msg": "File successfully deleted"}, status_code=status.HTTP_200_OK
    )


@app.post("/api/get-review/")
def get_resume_review(req: ReviewRequest):
    """
    Recieves file name for resume review from the frontend
    """
    print("\n")
    print(req, end="\n")
    if not req.file_name:
        return JSONResponse({"msg": "Error in File name"}, status_code=404)

    model = genai.GenerativeModel("gemini-1.5-pro")
    file = genai.upload_file(req.file_name)
    response = model.generate_content(
        [RESUME_REVIEW_PROMPT, req.job_description, JSON_RESPONSE_EXPECTED, file]
    )

    remove_resume_file(req)

    return {"msg": response.text}

