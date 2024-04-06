import google.generativeai as ai

#API Key
API_KEY = 'AIzaSyCVFpu2v_05mj0HStVllpNP5dIahRB51]Y'

# Configure the API
ai.configure(api_key=API_KEY)

# Create a new model
model = ai.GenerativeModel("gemini-pro")
chat = model.start_chat()

# Start a conversation
while True:
    message = input('you: ')
    if message. lower() == 'bye':
        print('Chatbot: Goodbye!')
        break
        response = chat.send_message(message)
        print('Chatbot:', response.text)



