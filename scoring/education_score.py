def calculate_education_score(candidate_field, jd_field):
    if candidate_field == "not specified":
        return 0

    if candidate_field in jd_field.lower():
        return 1.0

    return 0.5  # partial relevance