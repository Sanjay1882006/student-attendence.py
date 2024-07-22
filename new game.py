import math
import random
def try_():
    lower=int(input("Enter any number : "))
    upper=int(input("Enter a number grather than the first number : "))
    computer=math.log(upper-lower+1,2)
    computer=int(computer)
    random_=random.randint(lower,upper)
    print("you have",computer,"chans")
    while computer !=0:
        user_ans=int(input("enter your number : " ))
        if random_==user_ans:
            print("congratulation you win")
            computer-=1
            break
        elif random_>user_ans:
            print("your number is small")
            computer-=1
            print("you have",computer,"chance")
        else:
            print("your number is big")
            computer-=1
            print("you have",computer,"chance")
    if computer==0 and random_!= user_ans :
        print("sorry try again")
        print(random_, "is the right number")
    try_a=input("you wil try again, yes or no : ")
    if try_a=="yes":
        try_()
    else:
        print("bye")
try_()



