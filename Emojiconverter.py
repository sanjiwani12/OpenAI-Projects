from openai import OpenAI

client = OpenAI(api_key = "YOUR_OWN_API_KEY")

model = "gpt-4o-mini"

system_prompt = "You will be provided with text, and your task is to translate it into emojis. Do not use any regular text. Use emojis only."

user_prompt = input("Enter your prompt: ")

messages = [
    {
        "role": "system",
        "content": [
            {
                "type": "input_text",
                "text": system_prompt
            }
        ]
    },
    {
        "role": "user",
        "content": [
            {
                "type": "input_text",
                "text": user_prompt
            }
        ]
    },
]


response = client.responses.create(model=model, input = messages)

print(response.output_text)