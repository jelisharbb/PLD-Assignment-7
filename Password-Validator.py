# Program 2: Password validator
# Create a program that check if password is valid
# The password is valid if all criteria are met:
# a. Greater than 15 letters
# b. Have at least one capital letter
# c. Have at least one number
# d. Have at least one special char (~`!@#$%^&*()-_+={}[]|/\:;"'<>.,?)
# ex.
# input: P@ssw0rd+P@ssw0rd
# ouput: Valid

# Tip: loop through each character of the input then process it letter by letter

# greetings to the user
print ("\n\033[1mWELCOME TO JELISHA'S PASSWORD VALIDATOR\033[0m \n\nThe \033[92mpassword is valid\033[0m if all these criteria are met: \nA. Greater than \033[4m15 letters\033[0m \nB. Have at least \033[4mone capital letter\033[0m \nC. Have at least \033[4mone number\033[0m \nD. Have at least \033[4mone special character\033[0m (`~!@#$%^&*()-_=+[]|;:,<.>/?)")

# ask for input
userPass = input("\n\033[96mEnter your password here:\033[0m\n")

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
            userPass = input("\nYour password must be \033[91mgreater than 15 characters.\033[0m Please try again. \n\n\033[96mEnter your password here:\033[0m\n")
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
        # code that check if the password contains a special character
        for index in userPass:
            if index in "`~!@#$%^&*()-_=+[]|;:,<.>/?":
                specialCha += 1
                break
            else:
                continue
        if upper > 0 and number > 0 and specialCha > 0:
            valid1 = True
            break
        else:
            valid2 = True
    if valid1:
        break
    elif valid2:
        userPass = input("\n\033[1m\033[91mYour password is invalid.\033[0m It must contain at least \033[4mone uppercase letter\033[0m, \033[4mone number\033[0m, and \033[4mone special character\033[0m. Please try again. \n\n\033[96mEnter your password here:\033[0m\n")
        character = 0
        upper = 0
        number = 0
        specialCha = 0
        valid2 = False

if valid1:
    print ("\n\033[1m\033[92mYour password is valid.\033[0m\n")