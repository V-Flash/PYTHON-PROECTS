# Step 1
import random
from Hangman_Art import *
from Hangman_Words import word_list

#game logo
print(logo)

# number of chance user have to guess the word
life = 6

#ask user to start game
start_game = False

user_input = str(input("Do you want to start the game ?(Y/N): "))

if user_input == "N" or user_input == "n":
    pass
else:
    start_game = True


    # Randomly choose a word from the word_list and assign it to a variable called chosen_word.
    chosen_word = random.choice(word_list)
    print(chosen_word)

    # Create an empty List called display.
    display = []

    # For each letter in the chosen_word, add a "_" to 'display'.
    word_length = len(chosen_word)
    for _ in range(word_length):
        display += "_"

    while start_game:
        # Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
        player_input = str(input("guess a letter: ")).lower()

        # Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
        # If the letter at that position matches 'guess' then reveal that letter in the display at that position.
        for position in range(word_length):
            alpha = chosen_word[position]

            if alpha == player_input:
                display[position] = alpha

        if player_input not in chosen_word:
            life -=1
            print(f"The letter you guessed is not in the word: {player_input}")
            print(lives[life])
        if life == 0:
            print("You lose")
            break

        if player_input in display:
            print(f"You already guessed this letter: {player_input}")



        # Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
        print(display)

        if "_" not in  display:
            print("You Win!")
            print(lives[life])
            break

