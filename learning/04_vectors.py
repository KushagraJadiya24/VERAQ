import os 
import numpy as py
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
client = genai.client(api_key=os.getenv("GEMINI_API_KEY"))

#Iterate and Embed each document and store in a list
#ask a question and compare the cosine similarity
# retrieve the top value

