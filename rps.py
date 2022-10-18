import random
my_name=input("Enter your name : ")
def try_again():
    my_choise=input(my_name+" choise : ").lower().capitalize()
    computer=["Rock", "Paper", "Scissorse"]
    Your_choise=random.choice (computer)
    print("Computer input :",Your_choise)
    if Your_choise=="Rock":
        if my_choise=="Rock":
            print("Tie")
        elif my_choise=="Paper":
            print(my_name,"win")
        else:
            print("computer win")
    if Your_choise=="Paper":
        if my_choise=="Rock":
            print("computer win")
        elif my_choise=="Paper":
            print("tie")
        else:
            print(my_name,"win")
    if Your_choise=="Scissorse":
        if my_choise=="Rock":
            print(my_name,"win")
        elif my_choise=="Scissorse":
            print("tie")
        else:
            print("computer win")
    play=input("play again,yes or no : ")
    if play=="yes" or play=="YES" or play=="Yes":
        try_again()
    elif play=="no" or play=="NO" or play=="No":
        print("Good bay")
try_again()



