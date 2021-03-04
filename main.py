import random
from hangman_words import word_list
from hangman_art import logo, stages

game_is_on = True
lives = 6

#Randomly choose a word from the word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

print(logo)

#Testing code
#print(f'Pssst, the solution is {chosen_word}.')

#For each letter in the chosen_word, add a "_" to 'display'.
display = ["_" for letter in chosen_word]
print(display)

#GAME LOGIC
while game_is_on:
    print(logo)
    #Ask the user to guess a letter and assign their answer to a variable called guess.
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You've already guessed {guess}. Try again!")

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    print(f"{' '.join(display)}")
    if guess not in chosen_word:
        print(f"{guess} in not part of the word. You lose a life!")
        lives -= 1
    #win condition
    if "_" not in display:
        print("You win!")
        game_is_on = False
    #lose condition
    if lives == 0:
        print("You lose!")
        print(f"The word was {chosen_word}")
        game_is_on = False
    print(stages[lives])

