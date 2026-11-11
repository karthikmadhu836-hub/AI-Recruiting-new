def get_weights(role="default"):
    role = role.lower().replace(" ", "_")   # 🔥 FIX

    weight_config = {
        "data_analyst": {
            "skills": 0.4,
            "experience": 0.2,
            "education": 0.1,
            "semantic": 0.3
        },
        "software_engineer": {
            "skills": 0.35,
            "experience": 0.3,
            "education": 0.1,
            "semantic": 0.25
        },
        "quality_analyst": {   # ✅ NEW ROLE
            "skills": 0.3,
            "experience": 0.3,
            "education": 0.1,
            "semantic": 0.3
        },
        "default": {
            "skills": 0.3,
            "experience": 0.25,
            "education": 0.15,
            "semantic": 0.3
        }
    }

    return weight_config.get(role, weight_config["default"])