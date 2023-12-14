import google.generativeai as genai
import PIL.Image
import os

img = PIL.Image.open('test.jpg')

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel('gemini-pro-vision')

response = model.generate_content(["Tell me what this animal is thinking", img])

print(response.text)
