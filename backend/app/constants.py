"""
Python module that stores constant values to be used in the project.
"""

RESUME_REVIEW_PROMPT = """
                        You are an experienced HR with tech experience in the field of Computer Science, Data Science, Data Analysis and related fields. 
                        Your task is to review the provided resume against the job description.
                        Please share your thorough professional evaluation on whether the candidate's profile accurately matches with the job description.
                        Highlight the strengths and weaknesses of the applicant in relation to the specified job description.
                    """

JSON_RESPONSE_EXPECTED = """
                        Please provide a response as if you are telling the candidate, in the following JSON:
                        {
                            "description": "string - 100-150 words summarizing the match between job description and resume",
                            "formatting_description": "string - 80-100 words suggesting resume formatting improvements",
                            "percentage_match": "number - the overall percentage match between the job description and resume",
                            
                            "skills": {
                                "skills_matched": "string[] - list of specific skills from the resume that match the job description",
                                "skills_missing": "string[] - list of skills required in the job description but not found in the resume",
                                "critical_skills_not_present": "string[] - important 'must-have' skills from the job description that are missing",
                                "additional_skills_suggestion": "string[] - recommended skills to add based on industry or job role"
                            },
                            
                            "experience_relevance": {
                                "relevant_experience": "string[] - specific job experiences or projects from the resume that align with the job description",
                                "experience_gap": "string[] - gaps in relevant experience compared to the job description (e.g., years or industry experience)",
                                "closely_aligned_projects": "string[] - detailed descriptions of projects that match the role"
                            },

                            "education_match": {
                                "education_requirements_met": "boolean - does the resume meet or exceed educational requirements?",
                                "missing_education": "string[] - list of required degrees, certifications, or training missing in the resume",
                                "certifications_matched": "string[] - list of certifications from the job description found in the resume",
                                "certifications_missing": "string[] - certifications mentioned in the job description that are missing from the resume"
                            },
                            
                            "soft_skills_analysis": {
                                "soft_skills_matched": "string[] - list of soft skills from the resume that match the job description",
                                "soft_skills_missing": "string[] - list of important soft skills mentioned in the job description but missing from the resume"
                            },
                            
                            "job_title_relevance": {
                                "previous_job_titles_matched": "string[] - past job titles in the resume that align with the desired role",
                                "career_progression_fit": "string - analysis of whether the new role aligns with career progression based on work history"
                            },
                            
                            "language_and_tone": {
                                "language_match": "boolean - does the language and tone in the resume align with the job description (e.g., technical, creative, formal)?",
                                "action_verbs_matched": "string[] - list of action verbs from the resume that match job description expectations",
                                "tone_suitability": "string - evaluation of the resume tone (professional, technical, etc.) in relation to the job description"
                            },
                            
                            "achievements_vs_responsibilities": {
                                "achievements_highlighted": "string[] - list of measurable achievements in the resume that align with the job role",
                                "responsibilities_highlighted": "string[] - list of job responsibilities from the resume that are relevant to the job role",
                                "result_oriented_focus": "boolean - does the resume emphasize results (e.g., metrics, KPIs) over responsibilities?"
                            },
                            
                            "industry_match": {
                                "industry_keywords_matched": "string[] - keywords from the job description related to industry-specific experience found in the resume",
                                "industry_experience_gap": "string[] - areas where the user's industry experience does not align with job description"
                            },
                            
                            "years_of_experience": {
                                "years_of_experience_matched": "boolean - does the candidate's years of experience match the job requirements?",
                                "experience_level_fit": "string - analysis of whether the resume aligns with the seniority level described (e.g., junior, mid-level, senior)"
                            },
                            
                            "cultural_fit": {
                                "company_culture_alignment": "string - assessment of whether the resume reflects alignment with the company's culture based on job description (e.g., remote work, teamwork)",
                                "diversity_inclusion_reflected": "string[] - any experiences, qualifications, or certifications that show diversity and inclusion alignment"
                            },
                            
                            "job_description_match": {
                                "hard_requirements_met": "string[] - list of non-negotiable requirements (e.g., experience, skills) that are fulfilled by the resume",
                                "preferred_qualifications_matched": "string[] - optional or preferred qualifications in the job description that the candidate fulfills",
                                "requirements_missing": "string[] - list of essential requirements not found in the resume"
                            },
                            
                            "tailoring_suggestions": {
                                "resume_tailoring_advice": "string - recommendations for tailoring the resume to better match the job description (100-120 words)",
                                "role_specific_language_suggestions": "string[] - suggested improvements in resume wording to better reflect the role (e.g., stronger action verbs, role-related jargon)"
                            },
                            
                            "professional_summary_analysis": {
                                "summary_relevance": "boolean - does the professional summary align with the key job requirements?",
                                "missing_key_points": "string[] - list of important points missing from the resume's professional summary"
                            },
                            
                            "job_location_match": {
                                "location_suitability": "boolean - does the candidate’s location fit the job requirements (e.g., local, remote, relocation)?",
                                "remote_work_experience": "boolean - does the candidate have sufficient experience with remote or hybrid work?"
                            },
                            
                            "job_functionality_match": {
                                "primary_function_alignment": "boolean - does the candidate’s past job functions (e.g., management, development) match the job description?",
                                "function_gaps": "string[] - specific job functions the candidate lacks based on their resume"
                            },

                            "keywords_analysis": {
                                "keywords_matched": "string[] - list of job description keywords present in the resume",
                                "keywords_not_present": "string[] - list of important job description keywords missing from the resume",
                                "important_keywords_in_job_description": "string[] - critical keywords from the job description (hard and soft skills, technologies)",
                                "keywords_usage_suggestions": "string[] - recommendations for including missing keywords in the resume"
                            }
                        }

                    """
