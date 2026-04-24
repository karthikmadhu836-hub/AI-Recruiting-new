from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# -------- Convert text to embeddings --------
def get_embeddings(texts):
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform(texts)
    return vectors

# -------- Calculate similarity --------
def calculate_similarity(resume_text, jd_text):
    texts = [resume_text, jd_text]
    
    vectors = get_embeddings(texts)
    
    similarity = cosine_similarity(vectors[0:1], vectors[1:2])
    
    return float(similarity[0][0])