import random
user_name = input("Enter your name: ")

user_win = 0
computer_wins = 0

options =["rock", "paper", "scissors"]

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit ").lower()
    if user_input == "q":
        break

    if user_input not in options:
        continue

    random_num = random.randint(0,2)

    computer_pick = options[random_num] .lower()
    print("computer picked", computer_pick)

    if user_input == "rock" and computer_pick == "paper":
        print("paper covers rock!")
        computer_wins += 1

    elif user_input == "rock" and computer_pick == "scissors":
        print("rock smashes scissors!")
        user_win += 1

    elif user_input == "rock" and computer_pick == "rock":
        print("It is a tie!")

    elif user_input == "paper" and computer_pick == "rock":
        print("paper covers rock!")
        user_win += 1

    elif user_input == "paper" and computer_pick == "scissors":
        print("scissors cuts paper!")
        computer_wins += 1

    elif user_input == "paper" and computer_pick == "paper":
        print("It is a tie!")

    elif user_input == "scissors" and computer_pick == "rock":
        print("rock smashes scissors!")
        computer_wins += 1

    elif user_input == "scissors" and computer_pick == "paper":
        print("scissors cuts paper!")
        user_win += 1
    
    elif user_input == "scissors" and computer_pick == "scissors":
        print("It is a tie!")







    enter = input("Would you love to play again! ")

    name = ["yes", "yh", "yeah", "yep", "yes sir"]
    if enter in  name:
        continue

    user = "User score: " + str(user_win)
    computer = "Computer score: " + str(computer_wins)
    print(user)
    print(computer)