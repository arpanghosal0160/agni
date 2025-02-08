import openai

# Set your OpenAI API key
openai.api_key = 'sk-efgh5678abcd1234efgh5678abcd1234efgh5678'

def generate_response(prompt):
    response = openai.Completion.create(
        engine="davinci-codex",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

if __name__ == "__main__":
    user_prompt = input("Enter your prompt: ")
    response = generate_response(user_prompt)
    print("Response from LLM:", response)