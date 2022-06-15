from pickle import NONE
import random

#user_input =None

while True :
    user_input = int(input("please input your choice : "))
    num = random.randint(1,10)
    if num < user_input:
        print("too low")
    elif num > user_input :
        print(" too high")
    else :
        print("congratulate!! you win")
        play = input("do u wanna play again (y/n) ? ")
        if play == "y" :
            num= random.randint(1,10)
            user_input = None
        else :
            print("thnak u !!")
            break