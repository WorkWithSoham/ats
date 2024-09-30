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


# res = {
#     "description": "Your resume showcases a strong foundation in software engineering with experience in Java, Spring Boot, and various testing frameworks. You've demonstrated proficiency in agile methodologies and code quality tools, aligning well with many software development roles. However, to better target specific positions, consider tailoring your resume to highlight relevant projects and skills more prominently.",
#     "formatting_description": "Your resume is generally well-formatted but could benefit from some improvements. Consider adding spaces between job titles and companies for better readability. Additionally, consistently bolding company names would enhance visual appeal. Finally, structuring your skills section with clear categories (e.g., Programming Languages, Frameworks, Databases) would make it easier to quickly assess your expertise.",
#     "percentage_match": 75,
#     "skills": {
#         "skills_matched": [
#             "Python",
#             "TypeScript",
#             "JavaScript",
#             "Java",
#             "SQL",
#             "HTML",
#             "CSS",
#             "React",
#             "Django",
#             "Angular",
#             "NodeJS",
#             "Spring Boot",
#             "Express JS",
#             "MongoDB",
#             "MySQL",
#             "OracleDB",
#             "PostgreSQL",
#             "Microsoft Azure",
#             "Google Cloud",
#             "AWS",
#             "Git",
#             "Linux",
#             "Ubuntu",
#             "DBeaver",
#             "Datadog",
#             "Jira",
#             "TestNG",
#             "Jenkins",
#             "Docker",
#             "Swagger",
#             "Postman",
#             "IntelliJ",
#             "VS Code",
#             "Atom"
#         ],
#         "skills_missing": [],
#         "critical_skills_not_present": [],
#         "additional_skills_suggestion": [
#             "Kubernetes",
#             "Terraform",
#             "CI/CD tools (e.g., Jenkins, CircleCI)",
#             "Cloud platforms (e.g., AWS, Azure, GCP)"
#         ]
#     },
#     "experience_relevance": {
#         "relevant_experience": [
#             "Software Engineer Intern at Dematic",
#             "Full Stack Developer Intern at Oneworldlearners"
#         ],
#         "experience_gap": [],
#         "closely_aligned_projects": [
#             "JobStackz project utilizes Java, Spring Boot, Chrome API, and web scraping to extract job details, showcasing web development and data extraction skills.",
#             "Multi-Threading File Sync project, inspired by Dropbox and Google Drive, demonstrates experience with server-client architecture, UDP/TCP, File Watcher, and multi-threading."
#         ]
#     },
#     "education_match": {
#         "education_requirements_met": true,
#         "missing_education": [],
#         "certifications_matched": [],
#         "certifications_missing": []
#     },
#     "soft_skills_analysis": {
#         "soft_skills_matched": [
#             "Problem-solving",
#             "Teamwork",
#             "Communication"
#         ],
#         "soft_skills_missing": []
#     },
#     "job_title_relevance": {
#         "previous_job_titles_matched": [
#             "Software Engineer Intern",
#             "Full Stack Developer Intern"
#         ],
#         "career_progression_fit": "Your previous roles align well with entry-level software engineering positions. As you gain experience, consider targeting roles with increasing responsibility and specialization."
#     },
#     "language_and_tone": {
#         "language_match": true,
#         "action_verbs_matched": [
#             "Fixed",
#             "Resolved",
#             "Participated",
#             "Applied",
#             "Automated",
#             "Led",
#             "Supervised",
#             "Built",
#             "Formulated",
#             "Optimized",
#             "Leveraged",
#             "Achieved",
#             "Crafted"
#         ],
#         "tone_suitability": "The resume's tone is professional and technical, aligning well with software engineering roles."
#     },
#     "achievements_vs_responsibilities": {
#         "achievements_highlighted": [
#             "Fixed 50+ software defects",
#             "Resolved 30 high-priority issues",
#             "Improved system stability and performance",
#             "Automated 15+ unit and integration tests",
#             "Achieved a 70% success rate in endurance testing",
#             "Increased conversion by 32%",
#             "Led a team of 5 interns",
#             "Onboarded over 300 new clients",
#             "Reduced development time by 10%",
#             "Improved code quality",
#             "Achieved a 95% accuracy rate in job detail extraction"
#         ],
#         "responsibilities_highlighted": [
#             "Conducting a strategic blend of automated and manual testing",
#             "Optimizing software processes and overall project efficiency",
#             "Maintaining high code quality",
#             "Designing and implementing SaaS and Accounts Payable system features",
#             "Deploying a custom Learning Management System",
#             "Building reusable Python functions",
#             "Formulating a comprehensive Admin Dashboard",
#             "Migrating to a microservice architecture",
#             "Leveraging Spring Boot, JPA, TypeScript, and Chrome API web scraping techniques",
#             "Streamlining the application process for users",
#             "Crafting a Java project",
#             "Seamlessly integrating UDP/TCP, File Watcher, and multi-threading"
#         ],
#         "result_oriented_focus": true
#     },
#     "industry_match": {
#         "industry_keywords_matched": [
#             "Software Engineering",
#             "Full Stack Development",
#             "Agile",
#             "CI/CD",
#             "Testing",
#             "Code Quality",
#             "SaaS",
#             "Microservices",
#             "Web Scraping"
#         ],
#         "industry_experience_gap": []
#     },
#     "years_of_experience": {
#         "years_of_experience_matched": true,
#         "experience_level_fit": "The resume aligns with an entry-level or junior software engineer position due to the internship experiences."
#     },
#     "cultural_fit": {
#         "company_culture_alignment": "Based on the remote work experience highlighted, your resume demonstrates adaptability to different work environments, which is valuable for companies embracing flexible work arrangements.",
#         "diversity_inclusion_reflected": []
#     },
#     "job_description_match": {
#         "hard_requirements_met": [
#             "Strong foundation in Java",
#             "Experience with Spring Boot",
#             "Knowledge of testing frameworks",
#             "Familiarity with agile methodologies"
#         ],
#         "preferred_qualifications_matched": [
#             "Experience with cloud platforms (AWS, Azure, GCP)",
#             "Knowledge of CI/CD tools"
#         ],
#         "requirements_missing": []
#     },
#     "tailoring_suggestions": {
#         "resume_tailoring_advice": "To make your resume even stronger, tailor it to each specific job description. Highlight the projects and skills that directly align with the requirements of each role. For example, if a job requires experience with a particular cloud platform, emphasize your projects or experiences using that platform. Use keywords from the job description throughout your resume to demonstrate your relevance.",
#         "role_specific_language_suggestions": [
#             "Use industry-specific jargon relevant to the target role.",
#             "Quantify your achievements with specific metrics and results.",
#             "Incorporate keywords from the job description into your skills and experience sections."
#         ]
#     },
#     "professional_summary_analysis": {
#         "summary_relevance": false,
#         "missing_key_points": [
#             "A concise professional summary highlighting your key skills and career aspirations would strengthen your resume."
#         ]
#     },
#     "job_location_match": {
#         "location_suitability": true,
#         "remote_work_experience": true
#     },
#     "job_functionality_match": {
#         "primary_function_alignment": true,
#         "function_gaps": []
#     },
#     "keywords_analysis": {
#         "keywords_matched": [
#             "Software Engineer",
#             "Full Stack",
#             "Java",
#             "Spring Boot",
#             "Testing",
#             "Agile",
#             "CI/CD",
#             "Remote",
#             "Cloud",
#             "Microservices",
#             "Web Scraping"
#         ],
#         "keywords_not_present": [
#             "Problem-Solving",
#             "Teamwork",
#             "Communication"
#         ],
#         "important_keywords_in_job_description": [
#             "Software Engineer",
#             "Full Stack",
#             "Java",
#             "Spring Boot",
#             "Agile",
#             "Testing",
#             "Cloud",
#             "Microservices"
#         ],
#         "keywords_usage_suggestions": [
#             "Incorporate keywords like 'Problem-Solving', 'Teamwork', and 'Communication' naturally throughout your resume to highlight your soft skills."
#         ]
#     }
# }
