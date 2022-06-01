import random
import getpass

player_win = 0
computer_win = 0
score = int(input("how many time do u wanna play? : "))
name = input("your name : ")
while player_win < score and computer_win < score:
    print(f"player score: {player_win} and computer score : {computer_win}")
    print("*rock* \n*paper* \n*scissors*")
    choice = getpass.getpass(f"{name}'s move (hidden input): ").lower()
    if input == "quit" or input == "q":
        break
    while not (choice == "rock" or choice == "paper" or choice == "scissors"):
        choice = getpass.getpass(
            f"{name}'s input is wrong. please try again: ").lower()

    random_num = random.randint(1, 3)
    if random_num == 1:
        computer = "rock"
    elif random_num == 2:
        computer = "paper"
    else:
        computer = "scissors"

    print(f"{name}'s move : " + choice)
    print("computer's move : " + computer)
    print("Shoot!")

    if choice == computer:
        print("two players are tie")
    elif choice == "rock":
        if computer == "scissors":
            print(f"{name}'s player win")
            player_win += 1
        else:
            print("computer player win")
            computer_win += 1
    elif choice == "paper":
        if computer == "rock":
            print(f"{name}'s player win")
            player_win += 1
        else:
            print("computer player win")
            computer_win += 1
    elif choice == "scissors":
        if computer == "paper":
            print(f"{name}'s player win")
            player_win += 1
        else:
            print("computer player win")
            computer_win += 1
    else:
        print("enter valid input")
if player_win > computer_win :
    print(" congratulations boss!!")
else :
    print(" noo, what have you done!!")
print(f"final score : computer win {computer_win} times  and player win {player_win} times")