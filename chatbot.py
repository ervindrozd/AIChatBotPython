import random

print("Simple AI Bot (type 'exit' to quit)")

responses = {
    "hello": ["Hi!", "Hey!", "Hello there!"],
    "how are you": ["I'm good!", "Doing great!", "All fine here!"],
    "what is your name": ["I'm MiniBot.", "Call me Bot 😄"],
}

while True:
    user = input("You: ").lower()

    if user == "exit":
        print("Bot: Bye!")
        break

    found = False

    for key in responses:
        if key in user:
            print("Bot:", random.choice(responses[key]))
            found = True
            break

    if not found:
        print("Bot: I don't understand that yet.")
