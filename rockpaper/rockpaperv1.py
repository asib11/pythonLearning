print("*rock* \n*paper* \n*scissors*")
choice = input("player one : ")
choice2 = input ("player two: ")
print("Shoot!")
if choice == choice2:
    print("2players are tie")
elif choice or choice2:
    if choice == "rock" and choice2 == "scissors":
        print("1st player win")
    elif choice2 == "rock" and choice == "scissors":
        print("2nd player win")
    elif choice == "paper" and choice2 == "rock":
        print("1st player win")
    elif choice == "paper" and choice2 == "scissors":
        print("2nd player win")
    elif choice == "scissors" and choice2 == "paper":
        print("1st player win")
    else:
        print("2nd player win")
else : 
    print("enter valid input")