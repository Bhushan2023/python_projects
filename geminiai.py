import google.generativeai as genai
API_KEY = "AIzaSyBiGtq-MCH6S1hTMycQ4ah1-ERa54ruzu4"
genai.configure(api_key = API_KEY)

model = genai.GenerativeModel("gemini-2.0-flash")
chat = model.start_chat()

print("chat with Gemini! Type 'exit' to quit.")
while True:
    user_input = input("you:")
    if user_input.lower() == 'exit':
        break
    response = chat.send_message(user_input)
    print("geminiai", response.text)