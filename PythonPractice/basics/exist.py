""" My practice"""

import sys

# Create a list of names
thisList = ["khoo", "name", "fine"]

# Get user input
word = input("Enter a word to search: ")

# Check if the word is in the list or not
if word not in thisList:
    print(f"The list does not contain the string {word}")
    choice = input("Do you want to add the string to the list? (yes/no): ")
    if choice.lower() != "yes":
        sys.exit(-1)
    thisList.append(word)
    print(thisList)
    sys.exit(-1)
print(f"The list contains the string {word}")
choice = input("Do you want to delete the string from the list? (yes/no): ")
if choice.lower() != "yes":
    sys.exit(-1)
thisList.remove(word)
print(thisList)
