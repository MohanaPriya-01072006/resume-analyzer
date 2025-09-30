def recommend_jobs(skills):
    job_roles = {
        "AI Engineer": ["python", "machine learning", "nlp", "deep learning"],
        "Full Stack Developer": ["javascript", "react", "node", "html", "css"],
        "Data Analyst": ["sql", "excel", "statistics", "python", "visualization"]
    }
    recommendations = []
    for role, required in job_roles.items():
        match = len(set(skills).intersection(set(required)))
        if match > 1:
            recommendations.append(role)
    return recommendations
