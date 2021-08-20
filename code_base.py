import random
def getdate():
    import datetime
    return datetime.datetime.now()

def gaming():
    inp = input("Press S for Stone, P for Paper, or SC for Scissor..")
    print(f"Happy Gaming {name} !")
    game = ["Stone", "Paper", "Scissor"]
    ran = random.choice(game)
    # print(f"\nYou : {inp}")
    print()
    if inp =='S' or inp == 's':
        print("You : Stone")
    elif inp == 'p' or inp == 'P':
        print("You : Paper")
    elif inp == 'Sc' or inp == 'sc':
        print("You : Scissor")

    print(f"Computer : {ran}")

    if (inp == 's' or inp == 'S') and ran == "Scissor":
        print("Result : You win !")
    elif (inp == 'P' or inp =='p') and ran == "Stone":
        print("Result : You Win !")
    elif (inp =='Sc' or inp =='sc') and ran == "Paper":
        print("Result : You Win !")
    elif (inp == 'Sc' or inp == 'sc') and ran =="Stone":
        print("Result : You lose !")
    elif (inp == 'P' or inp == 'p') and ran == "Scissor":
        print("Result : You lose !")
    elif (inp == 'S' or inp == 's') and ran == "Paper":
        print("Result : You lose !")
    else:
        print("Result : Draw")

print("\t\t\t\t\t\t___WELCOME TO STONE PAPER SCISSOR___")
print("\t\t\t\t\t\t\t",getdate(),"\n")
name = input("Please enter your name: ")
gaming()
print("\nThanks for Playing :)")

num = int(input("Press 1 to play again or any other number to exit"))
if num == 1:
    gaming()
else:
    exit(0)
