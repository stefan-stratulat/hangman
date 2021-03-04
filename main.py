import random

game_is_on = True

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']


lives = 6


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

#GAME LOGIC
while game_is_on:
    #Ask the user to guess a letter and assign their answer to a variable called guess.
    guess = input("Guess a letter: ").lower()
    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    print(f"{' '.join(display)}")
    if guess not in chosen_word:
        lives -= 1
        print(f"Lives left: {lives}")
    #win condition
    if "_" not in display:
        print("You win!")
        game_is_on = False
    #lose condition
    if lives == 0:
        print("You lose!")
        game_is_on = False
    print(stages[lives])

