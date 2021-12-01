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
