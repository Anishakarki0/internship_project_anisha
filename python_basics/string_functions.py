# Function to count vowels and consonants in a string
#
def count_vowels_consonants(text):
    vowels = "aeiouAEIOU"
    v_count = 0
    c_count = 0
    for char in text:
        if char.isalpha():
            if char in vowels:
                v_count += 1
            else:
                c_count += 1
    return v_count, c_count

user_text = input("Enter a string: ")
v, c = count_vowels_consonants(user_text)
print(f"Vowels: {v}, Consonants: {c}")
