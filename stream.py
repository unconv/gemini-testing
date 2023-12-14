import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel('gemini-pro')

response = model.generate_content("Write a short poem about a cat", stream=True)

for chunk in response:
    print(chunk.text, end="", flush=True)

print()
