import random
import getpass

print("*rock* \n*paper* \n*scissors*")
name = input("your name : ")
choice = getpass.getpass(f"{name}'s move (hidden input): ").lower()
random_num = random.randint(1,3)
if random_num == 1:
    computer = "rock"
elif random_num == 2 :
    computer = "paper"
else :
    computer = "scissors"

print(f"{name}'s move : " + choice)
print("computer's move : "+ computer)
print("Shoot!")

if choice == computer :
    print("two players are tie")
elif choice == "rock" :
    if computer == "scissors":
        print(f"{name}'s player win")
    else : 
        print("computer player win")
elif choice == "paper" :
    if computer == "rock":
        print(f"{name}'s player win")
    else :
         print("computer player win")
elif choice == "scissors":                                 
    if computer == "paper" :
        print(f"{name}'s player win")
    else :
         print("computer player win")
else : 
    print("enter valid input")