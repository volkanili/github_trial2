def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"


def get_input(prompt):
    return input(prompt)


if __name__ == "__main__":
    user_name = get_input("Enter your name: ")
    user_greeting = get_input("Enter a greeting (leave empty for default): ")
    greeting = greet(user_name, user_greeting) if user_greeting else greet(user_name)
    print(greeting)
