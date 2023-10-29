import random
import string


def passwordGenerator(minLength, nos=True, spChars=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    chars = letters
    if nos:
        chars += digits
    if spChars:
        chars += special
    
    pwd = ""
    meets_criteria = False
    has_no = False
    has_spChars = False

    while ((not meets_criteria) or (len(pwd)<minLength)):
        newChar = random.choice(chars)
        pwd += newChar

        if newChar in digits:
            has_no = True
        if newChar in special:
            has_spChars = True

        meets_criteria = True
        if nos:
            meets_criteria = has_no
        if spChars:
            meets_criteria = meets_criteria and has_spChars

    return pwd


minlength = int(input("Enter min length of password: "))
hasNo = input("Do you want to include no.s (y/n)? ").lower() == 'y'
hasSpChars = input("Do you want to include spChars (y/n)? ").lower() == 'y'
print("Your password is: ", passwordGenerator(minlength, hasNo, hasSpChars))
