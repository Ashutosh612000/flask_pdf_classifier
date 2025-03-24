import torch

def transform_text(text, vectorizer):
    vector = vectorizer.transform([text]).toarray()
    return torch.tensor(vector, dtype=torch.float32)
