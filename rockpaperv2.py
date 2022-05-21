print("*rock* \n*paper* \n*scissors*")
choice = input("player one : ")
choice2 = input ("player two: ")
print("Shoot!")
if choice == choice2 :
    print("2players are tie")
elif choice or choice2 :
    if choice == "rock" :
        if choice2 == "scissors":
            print("1st player win")
        else :    
            print("2nd player win")
    elif choice == "paper" :
        if choice2 == "rock":
            print("1st player win")
        else :
             print("2nd player win")
    else:                                   #this condition belongs to scissors vs rest two
    #elif choice == "scissors" :
        if choice2 == "paper" :
            print("1st player win")
        else :
             print("2nd player win")
else : 
    print("enter valid input")