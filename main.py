import sys


def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"


def get_input(prompt):
    return input(prompt)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        user_name = sys.argv[1]
        user_greeting = sys.argv[2] if len(sys.argv) > 2 else ""
    else:
        user_name = get_input("Enter your name: ")
        user_greeting = get_input("Enter a greeting (leave empty for default): ")

    greeting = greet(user_name, user_greeting) if user_greeting else greet(user_name)
    print(greeting)
