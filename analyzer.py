import spacy
nlp = spacy.load("en_core_web_sm")

def analyze_resume(text):
    doc = nlp(text)
    skills = [ent.text for ent in doc.ents if ent.label_ in ["ORG", "PRODUCT", "SKILL"]]
    strengths = list(set([token.text for token in doc if token.pos_ == "NOUN"]))
    weaknesses = []  # Can add custom logic later
    return {
        "skills": skills,
        "strengths": strengths,
        "weaknesses": weaknesses
    }
