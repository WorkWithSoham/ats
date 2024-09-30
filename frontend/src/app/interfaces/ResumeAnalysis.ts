export interface ResumeAnalysis {
  description?: string;
  formatting_description?: string;
  percentage_match?: number;
  skills?: {
    skills_matched?: string[];
    skills_missing?: string[];
    critical_skills_not_present?: string[];
    additional_skills_suggestion?: string[];
  };
  experience_relevance?: {
    relevant_experience?: string[];
    experience_gap?: string[];
    closely_aligned_projects?: string[];
  };
  education_match?: {
    education_requirements_met?: boolean;
    missing_education?: string[];
    certifications_matched?: string[];
    certifications_missing?: string[];
  };
  soft_skills_analysis?: {
    soft_skills_matched?: string[];
    soft_skills_missing?: string[];
  };
  job_title_relevance?: {
    previous_job_titles_matched?: string[];
    career_progression_fit?: string;
  };
  language_and_tone?: {
    language_match?: boolean;
    action_verbs_matched?: string[];
    tone_suitability?: string;
  };
  achievements_vs_responsibilities?: {
    achievements_highlighted?: string[];
    responsibilities_highlighted?: string[];
    result_oriented_focus?: boolean;
  };
  industry_match?: {
    industry_keywords_matched?: string[];
    industry_experience_gap?: string[];
  };
  years_of_experience?: {
    years_of_experience_matched?: boolean;
    experience_level_fit?: string;
  };
  cultural_fit?: {
    company_culture_alignment?: string;
    diversity_inclusion_reflected?: string[];
  };
  job_description_match?: {
    hard_requirements_met?: string[];
    preferred_qualifications_matched?: string[];
    requirements_missing?: string[];
  };
  tailoring_suggestions?: {
    resume_tailoring_advice?: string;
    role_specific_language_suggestions?: string[];
  };
  professional_summary_analysis?: {
    summary_relevance?: boolean;
    missing_key_points?: string[];
  };
  job_location_match?: {
    location_suitability?: boolean;
    remote_work_experience?: boolean;
  };
  job_functionality_match?: {
    primary_function_alignment?: boolean;
    function_gaps?: string[];
  };
  keywords_analysis?: {
    keywords_matched?: string[];
    keywords_not_present?: string[];
    important_keywords_in_job_description?: string[];
    keywords_usage_suggestions?: string[];
  };
}
