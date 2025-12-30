from openai import OpenAI

client = OpenAI(api_key="sk-YOUR-API-KEY")

model = "gpt-4o-mini"

user_prompt = input("Enter your prompt: ")

response = client.responses.create(model=model, input=user_prompt)

print(response.output_text)



