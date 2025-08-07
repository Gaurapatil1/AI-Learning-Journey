# AI Day 1 Bot
# user_input = input("You: ")

# if "weather" in user_input.lower():
#     print("Bot: It's sunny today!")
# elif "your name" in user_input.lower():
#     print("Bot: I'm a simple AI bot.")
# elif "bye" in user_input.lower():
#     print("Bot: Goodbye!")
# else:
#     print("Bot: Sorry, I don't understand.")  


# AI Day 1 Bot (with continuous chat loop)

print("Bot: Hello! Ask me something (type 'bye' to exit)")

while True:
    user_input = input("You: ")

    if "bye" in user_input.lower():
        print("Bot: Goodbye!")
        break
    elif "weather" in user_input.lower():
        print("Bot: It's sunny today!")
    elif "your name" in user_input.lower():
        print("Bot: I'm a simple AI bot.")
    elif "help" in user_input.lower():
        print("Bot: How can I assist you today?")
    elif "joke" in user_input.lower():
        print("Bot: Why did the scarecrow win an award? Because he was outstanding in his field!")
    elif "help" in user_input.lower():
        print("Bot: How can I assist you today?")
    elif "joke" in user_input.lower():
        print("Bot: Why did the scarecrow win an award? Because he was outstanding in his field!")
    elif "help" in user_input.lower():
        print("Bot: How can I assist you today?")
    elif "joke" in user_input.lower():
        print("Bot: Why did the scarecrow win an award? Because he was outstanding in his field!")
    elif "help" in user_input.lower():
        print("Bot: How can I assist you today?")
    elif "joke" in user_input.lower():
        print("Bot: Why did the scarecrow win an award? Because he was outstanding in his field!")
    elif "help" in user_input.lower():
        print("Bot: How can I assist you today?")
    
       
    elif "time" in user_input.lower():
        from datetime import datetime
        current_time = datetime.now().strftime("%H:%M:%S")
        print(f"Bot: The current time is {current_time}.")

    else:
        print("Bot: Sorry, I don't understand.")
