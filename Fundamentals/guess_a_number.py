import random

computer_number = random.randint(1, 100)

while True:
    player_input = input("Guess the number (1 - 100): ")

    if not player_input.isdigit():
        print("Invalid input. You must use only numbers and not letters !")
        continue
    else:
        player_input = int(player_input)

    if player_input > 100 or player_input < 1:
        print("Invalid input! Number must be in region between 1 and 100 !")

    elif player_input == computer_number:
        print("You guess it!")
        print("Thanks for playing !!!")
        break
    elif player_input > computer_number:
        print("Too high!")
    else:
        print("Too low!")


