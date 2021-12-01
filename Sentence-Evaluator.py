# Create a program that ask for a sentence as input.
# Display the number of words, vowels and consonants in the input 

# greetings to the user
print ("\n\033[7mWelcome! This program will count the number of words, vowels, and consonants in your input.\033[0m")

# ask for input
userInput = input("\nEnter your \033[4mtext\033[0m here:\n")

# variables to be used
wordCount = 1
vowelCount = 0
consonantCount = 0

# code for character counting
for index in userInput.upper():
    if index in 'AEIOU':
        vowelCount += 1
    elif index in 'BCDFGHJKLMNPQRSTVWXYZ':
        consonantCount += 1
    elif index in ' ':
        wordCount += 1

# result
print (f"\n\033[1m\033[96mWord/s:\033[0m \033[1m{wordCount}\033[0m \n\033[1m\033[95mVowel/s:\033[0m \033[1m{vowelCount}\033[0m \n\033[1m\033[91mConsonant/s:\033[0m \033[1m{consonantCount}\033[0m \n")