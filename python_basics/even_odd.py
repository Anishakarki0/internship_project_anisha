# Program to check if a number is even or odd

def check_even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

try:
    user_input = int(input("Enter a number: "))
    print(f"The number {user_input} is {check_even_odd(user_input)}")
except ValueError:
    print("Invalid input! Please enter an integer.")
