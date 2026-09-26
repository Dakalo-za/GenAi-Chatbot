from google import genai

client = genai.Client(api_key = "")

print('The Genai chatbot is ready, type "quit" to stop"\n')

while True:
    user_input = input('You: ')
    if user_input.lower() == "quit":
        print("Goodbye")
        break

    response = client.models.generate_content(
        model = "gemini-3.8-flash",
        contents = user_input
    )

    print("Chatbot: ", response.text)