from src.describe_image import describe_image


def simple_chatbot():
    print("Hello! I'm a multi-modal chatbot. Type something and I'll respond. Type 'exit' to leave the chat.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            # TODO: extact img filepath
            print("Chatbot: Goodbye! Have a great day!")
            break
        else:
            print(f"Chatbot: You said '{user_input}'. That's interesting!")


if __name__ == "__main__":
    # TODOs
    # (1) Write simple unit tests for describe_image() + helper funcs
    # (2) Separate image filepath from rest of user input
    # (3) Feed image_filepath -> describe_image() --> image_description --> gemma
    # (4) Center + crop image rather than resizing it
    # (5) Make a simple demo

    # How to generate description of image from image_filepath
    image_path = "src/images/cat.jpg"
    image_description = describe_image(image_path)
    print(image_description)
