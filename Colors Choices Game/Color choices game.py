# import random module
import random

computer_score = 0
player_score = 0

print("red = 1 \nyellow = 2 \norange = 3 \ngreen = 4 \nblue = 5 \ntake a turn: ")

while True:

    player_choice = int(input("user turn:"))

    while player_choice > 5 or player_choice < 1:
        player_choice = int(input("Enter vaild number:"))

    if player_choice == 1:
        player_sel = "red"
    elif player_choice == 2:
        player_sel = "yellow"
    elif player_choice == 3:
        player_sel = "orange"
    elif player_choice == 4:
        player_sel = "green"
    else:
        player_sel = "blue"

    print("User select:"+player_sel)
    print("\nComputer Turn")
    print("Computer choosing colour...")

    computer_choice = random.randint(1, 5)

    while computer_choice == player_choice:
        computer_choice = random.randint(1, 5)

    if computer_choice == 1:
        comp_sel = "red"
    elif computer_choice == 2:
        comp_sel = "yellow"
    elif computer_choice == 3:
        comp_sel = "orange"
    elif computer_choice == 4:
        comp_sel = "green"
    else:
        comp_sel = "blue"

    print("Computer select:"+comp_sel)

    if player_sel == comp_sel:
        player_score +=1
        print("\nplayer score ="+ str(player_score))
        print("computer score =" + str(computer_score))
    else:
        computer_score += 1
        print("\nplayer score = " + str(player_score))
        print("computer score = " + str(computer_score))

    print("Do you want to play again? Y/N")

    answer = input()

    if answer == "n" or answer == "N":
        break

    if player_score == computer_score:
        print("Game Tied")
    elif player_score > computer_score:
        print("User Win")
    else:
        print("Computer Win")

    print("\nThank You for Playing!")



