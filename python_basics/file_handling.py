
# Task: Read data from a text file and count lines and words
# Author: Anisha Karki

file_path = "C:/Users/dell/OneDrive/Desktop/Anisha/internship_project_anisha/python_basics/sample.txt"

try:
    with open(file_path, "r") as file:
        lines = file.readlines()
        total_lines = len(lines)
        total_words = sum(len(line.split()) for line in lines)
    
    print("File read successfully!")
    print(f"Total lines in the file: {total_lines}")
    print(f"Total words in the file: {total_words}")

except FileNotFoundError:
    print(f"File not found! Make sure '{file_path}' exists in your folder.")
except Exception as e:
    print(f"Oops! Something went wrong: {e}")
