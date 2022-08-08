# import random module
import random

print("Winning Rules of the Colors choices Game as follows: "+ "\nEnter a number from one two five and match computer choice to Win the computer.")
computer_score = 0
player_score = 0

while True:
    print("red = 1 \nyellow = 2 \norange = 3 \ngreen = 4 \nblue = 5 \ntake a turn: ")

    # take the input from user
    player_choice = int(input("User turn: "))



    # looping until user enter invalid input
    if player_choice > 5 and player_choice < 1:
        player_choice = int(input("enter valid input: "))


    if player_choice == 1:
        choice_col = 'red'
    elif player_choice == 2:
        choice_col = 'yellow'
    elif player_choice == 3:
        choice_col = 'orange'
    elif player_choice == 4:
        choice_col = 'green'
    else:
        choice_col = 'blue'

    # print user choice
    print("user color choice is: " + choice_col)
    print("\nNow its computer turn to choose a color.......")

    computer_choice = random.randint(1, 5)

    while computer_choice == player_choice:
        computer_choice = random.randint(1, 5)

    if player_choice == 1:
        comp_choice_col = 'red'
    elif player_choice == 2:
        comp_choice_col = 'yellow'
    elif player_choice == 3:
        comp_choice_col = 'orange'
    elif player_choice == 4:
        comp_choice_col = 'green'
    else:
        comp_choice_col = 'blue'

    print("Computer color choice is: " + comp_choice_col)

    if choice_col == comp_choice_col:
        player_score += 1
        print("player_score: " + str(player_score))
        print("computer_score: " + str(computer_score))
    else:
        computer_score += 1
        print("player_score: " + str(player_score))
        print("computer_score: " + str(computer_score))

    print("Do you want to play again? (Y/N)")
    answer = input()

    if answer == 'n' or answer == 'N':
        break

    if computer_score == player_score:
        print("Game is Tied")
        print("\nThanks for playing")
    elif computer_score < player_score:
        print("Player is Victorious")
        print("<== User wins ==>")
        print("\nThanks for playing")
    elif computer_score > player_score:
        print("\n<== Computer wins ==>")
        print("\nPlayer is Defeated")
        print("\nThanks for playing")
