# Create a program that ask for a sentence as input.
# Display the number of words, vowels and consonants in the input 

# greetings to the user
print ("\nWelcome! This program will count the number of words, vowels, and consonants in your input.")

# ask for input
userInput = input("\nEnter you text here: ")

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
print (f"\nWord/s: {wordCount} \nVowel/s: {vowelCount} \nConsonant/s: {consonantCount} \n")