
# Task -Accept 5 numbers from the user, find the maximum and average

numbers_list = []

print("Hi! Let's enter 5 numbers and I’ll calculate the max and average for you.")

for i in range(5):
    while True:
        try:
            user_input = float(input(f"Enter number {i+1}: "))
            numbers_list.append(user_input)
            break
        except ValueError:
            print("That’s not a number! Please enter a valid number.")

print("Calculating results...")
maximum_number = max(numbers_list)
average_number = sum(numbers_list) / len(numbers_list)

print(f"Numbers you entered: {numbers_list}")
print(f"The maximum number is: {maximum_number}")
print(f"The average of these numbers is: {average_number}")
