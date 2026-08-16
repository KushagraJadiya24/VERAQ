import os
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