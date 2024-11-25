from openai_api.utils import describe_image

def simple_chatbot():
    print("Hello! I'm a multi-modal chatbot. Type something and I'll respond. Type 'exit' to leave the chat.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            # TODO: get user response
            print("Chatbot: Goodbye! Have a great day!")
            break
        else:
            print(f"Chatbot: You said '{user_input}'. That's interesting!")

# Run the chatbot
if __name__ == "__main__":
    image_path = "openai_api/images/cat.jpg"
    image_description = describe_image(image_path)
    print(image_description)
