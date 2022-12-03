def dummy_chatbot():
    while True:
        print("Hi! Do you want to talk to me?")
        reply = input()
        if reply == "no":
            break
        print("That's cool!")
    print("All right, bye!")
dummy_chatbot()
