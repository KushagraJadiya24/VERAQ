import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
def ask_llm(prompt):
    try:
        response = client.models.generate_content(
            model="gemini-3.5-flash-lite",
            contents=prompt,
            config={
                "system_instruction": "You are a Dragon. Answer like a dragon",
                "temperature": 1}
        )
     
        return response.text
    except Exception as e:
        return f"Request failed: {e}"

if __name__ == "__main__":
        answer = ask_llm("hi, how are you")
        print(answer)