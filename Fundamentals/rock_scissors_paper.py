import random


computer_move = ""

rock = "Rock"
scissor = "Scissors"
paper = "Paper"


player_move = input("Choose [r]ock, [p]aper, [s]cissors:")

if player_move == "r" or player_move == "R":
    player_move = rock

elif player_move == "p" or player_move == "P":
    player_move = paper

elif player_move == "s" or player_move == "S":
    player_move = scissor

else:
    raise SystemExit("Invalid input. Try again....")

computer_random_number = random.randint(1,3)

if computer_random_number == 1:
    computer_move = "Rock"
elif computer_random_number == 2:
    computer_move = "Paper"
else:
    computer_move = "Scissors"

print(f"You chose {player_move}")
print(f"The computer's choice is {computer_move}")

if (player_move == rock and computer_move == scissor) or (player_move == paper and computer_move == rock) or\
        (player_move == scissor and computer_move == paper):
    print("You win!")

elif player_move == computer_move:
    print("Draw!")

else:
    print("You lose!")


