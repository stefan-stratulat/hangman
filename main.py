import random

#list of words for the game
word_list = ["aardvark", "baboon", "camel"]

#Randomly choose a word from the word_list and assign it to a variable called chosen_word.

chosen_word = random.choice(word_list)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')


#For each letter in the chosen_word, add a "_" to 'display'.

display = ["_" for letter in chosen_word]
print(display)

#Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess = input('Guess a letter: ').lower()

#Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

#If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].

display = [guess if letter == guess else "_" for letter in chosen_word]
print(display)
