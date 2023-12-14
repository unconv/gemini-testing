import requests
import json
import sys
import os

import gemini_functions

api_key = os.getenv("GOOGLE_API_KEY")

def parse_function_response(message):
    function_call = message[0]["functionCall"]
    function_name = function_call["name"]

    print("Gemini: Called function " + function_name )

    try:
        arguments = function_call["args"]

        if hasattr(gemini_functions, function_name):
            function_response = getattr(gemini_functions, function_name)(**arguments)
        else:
            function_response = "ERROR: Called unknown function"
    except TypeError:
        function_response = "ERROR: Invalid arguments"

    return (function_name, function_response)


def run_conversation(message, messages = []):
    messages.append(message)

    with open("messages.json", "w") as f:
        f.write(json.dumps(messages, indent=4))

    data = {
        "contents": [messages],
        "tools": [{
            "functionDeclarations": gemini_functions.definitions
        }]
    }

    response = requests.post("https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key="+api_key, json=data)

    if response.status_code != 200:
        print(response.text)
        print("ERROR: Unable to make request")
        sys.exit(1)

    response = response.json()

    if "content" not in response["candidates"][0]:
        print("ERROR: No content in response")
        print(response)
        sys.exit(1)

    message = response["candidates"][0]["content"]["parts"]
    messages.append({
        "role": "model",
        "parts": message
    })

    if "functionCall" in message[0]:
        function_name, function_response = parse_function_response(message)

        message = {
            "role": "function",
            "parts": [{
                "functionResponse": {
                    "name": function_name,
                    "response": {
                        "name": function_name,
                        "content": function_response
                    }
                }
            }]
        }
    else:
        user_message = input("Gemini: " + message[0]["text"] + "\nYou: ")
        message = {
            "role": "user",
            "parts": [{"text": user_message}]
        }

    run_conversation(message, messages)

messages = []

system_message = "You are an AI bot that can do everything using function calls. When you are asked to do something, use the function call you have available and then respond with a message shortly confirming what you have done. When writing code, write fully functional code. When writing to files, give only a relative path like dir/file or just the basename."

user_message = input("Gemini: What do you want to do?\nYou: ")
message = {
    "role": "user",
    "parts": [{"text": system_message + "\n\n" + user_message}]
}

run_conversation(message, messages)
