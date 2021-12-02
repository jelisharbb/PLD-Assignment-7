# Program 2: Password validator
# Create a program that check if password is valid
# The password is valid if all criteria are met:
# a. Greater than 15 letters
# b. Have at least one capital letter
# c. Have at least one number
# d. Have at least one special char (!@#$%^&*()_+ etc) (~`!@#$%^&*()-_+={}[]|/\:;"'<>.,?)
# ex.
# input: P@ssw0rd+P@ssw0rd
# ouput: Valid

# Tip: loop through each character of the input then process it letter by letter

# greetings to the user
print ("\nWELCOME TO JELISHA'S PASSWORD VALIDATOR \n\nThe password is valid if all these criteria are met: \nA. Greater than 15 letters \nB. Have at least one capital letter \nC. Have at least one number \nD. Have at least one special character (!@#$%^&*()_+ etc)")

# ask for input
userPass = input("\nEnter your password here:\n")

character = 0
upper = 0
number = 0
specialCha = 0

valid1 = False
valid2 = False

# while loop code if the password is greater than 15 characters
while not valid1:
    while len(userPass) <= 15:
        if len(userPass) <= 15:
            userPass = input("\nYour password must be greater than 15 characters. Please try again. \nEnter your password here: ")
            if len(userPass) > 15:
                break
    while not valid2:
        # code that checks if the password has an uppercase letter
        for index in userPass:
            if index in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                upper += 1
                break
            else:
                continue
        # code that checks if the password contains a number
        for index in userPass:
            if index in '0123456789':
                number += 1
                break
            else:
                continue