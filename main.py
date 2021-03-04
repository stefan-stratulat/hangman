import random

#list of words for the game
word_list = ["aardvark", "baboon", "camel"]

#Randomly choose a word from the word_list and assign it to a variable called chosen_word.

chosen_word = random.choice(word_list)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#TODO-1: - Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"]
# with 5 "_" representing each letter to guess.

display = ["_" for letter in chosen_word]
print(display)

#Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess = input('Guess a letter: ').lower()

#Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

for letter in chosen_word:
    if letter == guess:
        print('Right')
    else:
        print('Wrong')
