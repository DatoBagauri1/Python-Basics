import random
while True:
    list="rock","paper","scissors"
    computer=random.choice(list)
    player=input("enter rock, paper, or scissors-")
    if player==computer:
        print("tie")
    elif player=="rock" and computer=="scissors":
        print("you win")
    elif player=="scissors" and computer=="rock":
        print("you lose")
    elif player=="paper" and computer=="rock":
        print("you win")
    elif player=="scissors" and computer=="paper":
        print("you win")
    elif player!="rock" or "paper" or "scissors":
        print("only type rock, paper, or scissors!!!!!!")

    else:
        print("you lose")
    print("computer-",computer)
    print("player-",player)
    playagain=input("do you want to play again? (yes/no)")
    if playagain!="yes":
        break
print("bye")