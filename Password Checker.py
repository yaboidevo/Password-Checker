from time import sleep

special_characters = ["!", "#", "$", "%", "&",  "’", "(", ")", "*", "+", ",", "-", ".", "/", ":", ";", "<", "=", ">", "?", "@", "[", "]", "^", "_", "`", "{", "|", "}", "~"]

print("Welcome to password security check!\n")
password = input("Enter the password: ")
print("\nAnalyzing Data...")

if len(password) < 7:
    sleep(2)
    print("\nPassword is too short.")

if not any(character.isdigit() for character in password):
    sleep(2)
    print("\nPassword doesn't contain a number")

if any(substring in password for substring in ["123", "abc", "qwe", "asd", "zxc"]):
    sleep(2)
    print("\nAvoid commonly used keyboard substrings.")

if all(char not in password for char in special_characters):
    sleep(2)
    print("\nPassword doesn't contain a special character")

else:
    sleep(2)
    print("\nPassword is secure!")
