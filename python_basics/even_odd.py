# Task: Check if a number is even or odd

try:
    user_number = int(input("Hello! Enter a number to see if it's even or odd: "))
    print("Checking your number...")
    if user_number % 2 == 0:
        print(f"Great! {user_number} is an even number.")
    else:
        print(f"{user_number} is an odd number. Interesting!")
except ValueError:
    print("Oops! That wasn’t a valid integer. Please try again.")
