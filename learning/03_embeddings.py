import os
import numpy as np

from dotenv import load_dotenv
from google import genai

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def get_embedding(text):
    response = client.models.embed_content(
        model="gemini-embedding-001",
        contents=text
    )
    return response.embeddings[0].values

# get embeddings for these two related words
vec1 = get_embedding("dog")
vec2 = get_embedding("puppy")

print(len(vec1))   # how many numbers are in the vector?
print(vec1[:5])    # print just the first 5 numbers to peek at it

def cosine_similarity(vec1, vec2):
    vec1 = np.array(vec1)
    vec2 = np.array(vec2)

    dot_product = np.dot(vec1, vec2)
    magnitude1 = np.linalg.norm(vec1)
    magnitude2 = np.linalg.norm(vec2)

    return dot_product / (magnitude1 * magnitude2)

vec_dog = get_embedding("dog")
vec_puppy = get_embedding("puppy")
vec_banana = get_embedding("banana")

print("dog vs puppy:", cosine_similarity(vec_dog, vec_puppy))
print("dog vs banana:", cosine_similarity(vec_dog, vec_banana))