import random
import string

def generate_password(min_length,letter=True,numbers=True,special_character=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = []
    if letter:
        characters+=letters
    if numbers:
        characters+=digits
    if special_character:
        characters+=special
    pwd = ""
    meets_criteria = False
    has_number = False
    has_special =False
    has_letter = False

    while not meets_criteria or len(pwd)<min_length:
        new_char = random.choice(characters)
        pwd+=new_char
        if new_char in digits:
            has_number = True
        if new_char in special:
            has_special = True
        if new_char in letters:
            has_letter = True
        if has_special and has_special and has_letter:
            meets_criteria = True
    print("Your password is successfully generated")
    print(f"Your password is {pwd}")

l= input("Do you want your password to contain letter [y/n]").lower() == "y"
n= input("Do you want your password to contain numbers [y/n]").lower() == "y"
s= input("Do you want your password to contain special characters [y/n]").lower() == "y"
num = int(input("Enter the minimum length of the password"))
generate_password(num,l,n,s)
