import getpass

print("*rock* \n*paper* \n*scissors*")

choice = getpass.getpass ( "player one : ")
choice2 = getpass.getpass ( "player two: ")
print("Shoot!")
print("player 1's move : " + choice)
print("player 2's move : " + choice2)

if choice == choice2 :
    print("2players are tie") 
elif choice == "rock" :
    if choice2 == "scissors":
        print("1st player win")
    elif choice2 =="paper" :    
        print("2nd player win")
elif choice == "paper" :
    if choice2 == "rock":
        print("1st player win")
    elif choice2 == "scissors" :
         print("2nd player win")                                  
elif choice == "scissors" :
    if choice2 == "paper" :
        print("1st player win")
    elif choice2 == "rock" :
         print("2nd player win")
else : 
    print("enter valid input")