
import random
import string


print("Random Password Generator \n")
def get_characters():
    characters = ''
    include_lower = input("Include lowercase letters? (y/n): ").lower()
    if include_lower == 'y':
        characters += string.ascii_lowercase

    include_upper = input("Include uppercase letters? (y/n): ").lower()
    if include_upper == 'y':
        characters += string.ascii_uppercase

    include_digits = input("Include numbers? (y/n): ").lower()
    if include_digits == 'y':
        characters += string.digits

    include_special = input("Include special characters? (y/n): ").lower()
    if include_special == 'y':
        characters += string.punctuation

    if characters == '':
        print("\nNo character sets selected. Using lowercase by default.\n")
        characters = string.ascii_lowercase

    return characters


try:
    length_input = input("\nEnter desired password length: ")
    length = int(length_input)

    if length <= 0:
        print("Password length should be greater than 0.")
    else:
        
        char_pool = get_characters()

        
        password = ''
        for i in range(length):
            random_char = random.choice(char_pool)
            password += random_char

        
        print("\nYour generated password is:")
        print(password)
except ValueError:
    print("Please enter a valid number for the password length.")
except Exception as e:
    print("Something went wrong:", e)
