import os 
import numpy as np
from dotenv import load_dotenv
from google import genai

documents = [
    "The Eiffel Tower is located in Paris, France.",
    "Python is a popular programming language for AI.",
    "The mitochondria is the powerhouse of the cell.",
    "Cats are popular pets known for their independence.",
    "Machine learning models require large datasets to train."
]

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

#Iterate and Embed each document and store in a list
#ask a question and compare the cosine similarity
# retrieve the top value
vectors =[]
def embed(text):
    response = client.models.embed_content (
            model="gemini-embedding-001",
            contents=text
        )
    return response.embeddings[0].values


question = "What is a common pet?"
q = embed(question)

def compare(vec1,vec2):
    vec1 = np.array(vec1)
    vec2=np.array(vec2)

    dot_product = np.dot(vec1,vec2)
    magnitude1 = np.linalg.norm(vec1)
    magnitude2 = np.linalg.norm(vec2)
    
    return dot_product / (magnitude1 * magnitude2)

vals = []
best_score=0

for str in documents:
    print(str)
    vals.append(compare(q,embed(str)))
    if vals[len(vals)-1]>best_score:
        best_score = vals[len(vals)-1]
        best_val = str
    print(vals[len(vals)-1])

prompt = f"Answer the question using only this context.\n\nContext: {best_val}\n\nQuestion: {question}"


def ask_llm(prompt):
    try:
        response = client.models.generate_content(
            model="gemini-3.5-flash-lite",
            contents=prompt,
        )
        return response.text
    except Exception as e:
        return f"Request failed: {e}"

answer = ask_llm(prompt)
print(answer)