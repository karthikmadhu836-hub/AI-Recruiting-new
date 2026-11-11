from ats_engine.skill_extractor import extract_skills_with_confidence


def test_skill_extraction():
    text = "Python Django React MERN communication"

    skills = extract_skills_with_confidence(text)

    print("\nExtracted Skills:", skills)

    # Test 1: Skills should not be empty
    assert len(skills) > 0, "❌ No skills extracted"

    # Test 2: Python should be detected
    assert any(s["skill"] == "python" for s in skills), "❌ Python not detected"

    # Test 3: Confidence should exist
    assert all("confidence" in s for s in skills), "❌ Confidence missing"

    print("✅ Skill extraction test PASSED")