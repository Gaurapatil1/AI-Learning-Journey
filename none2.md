# Lists
fruits = ["apple", "banana", "mango"]
print("First fruit:", fruits[0])
fruits.append("orange")
print("Fruits after adding orange:", fruits)

# Tuples
coordinates = (10, 20)
print("X coordinate:", coordinates[0])

# Dictionaries
student = {"name": "Gaurav", "age": 19}
print("Student name:", student["name"])
student["age"] = 20
print("Updated student info:", student)

# Sets
countries = {"India", "USA", "India"}
print("Unique countries:", countries)

# Mini Chatbot Example
responses = {
    "hi": "Hello! How can I help you today?",
    "bye": "Goodbye! Have a great day!",
    "name": "I am a simple AI bot."
}

user_input = input("You: ").lower()
print("Bot:", responses.get(user_input, "Sorry, I don't understand."))