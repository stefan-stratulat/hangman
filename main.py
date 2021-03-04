import random

game_is_on = True

#list of words for the game
word_list = ["aardvark", "baboon", "camel"]

#Randomly choose a word from the word_list and assign it to a variable called chosen_word.

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#For each letter in the chosen_word, add a "_" to 'display'.

display = ["_" for letter in chosen_word]
print(display)

#TODO-1: - Use a while loop to let the user guess again.
#The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_").
#Then you can tell the user they've won.


while game_is_on:
    #Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
    guess = input("Guess a letter: ").lower()
    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    print(display)
    if "_" not in display:
        print("You win!")
        game_is_on = False

