import random, time
print("Let us play RPS game")
while True:
    print("Enter choice \n1. Rock\n2. Paper\n3. Scissor")
    choice=int(input("User turn: "))
    while choice > 3 or choice < 1:
        choice=int(input("enter valid input: "))
    if choice == 1:
        choice_name = "Rock"
    elif  choice == 2:
        choice_name = "Paper"
    else:
        choice_name = "Scissor"
    print("User Choice is: "+ choice_name)
    print("Now its computerji's turn....")
    comp_choice = random.randint(1,3)
    time.sleep(1)
    while comp_choice == choice:
        comp_choice = random.randint(1,3)
    if comp_choice == 1:
        comp_choice_name = "Rock"
    elif comp_choice == 2:
        comp_choice_name = "Paper"
    else:
        comp_choice_name = "Scissors"
    print("ComputerJi's Choice is: "+ comp_choice_name)
    #Gameplay
    print(choice_name + " V/S " + comp_choice_name)
    time.sleep(1)
    if((choice == 1 and comp_choice == 2) or (choice == 2 and comp_choice == 1)):
        print("Paper Wins.")
        result = "paper"
    elif((choice==1 and comp_choice == 3) or (choice == 3 and comp_choice == 1)):
        print("Rock Wins.")
        result = "rock"
    else:
        print("Scissor Wins.")
        result = "scissor"
    time.sleep(1)
    if result == choice_name:
        print("User Wins.")
    else:
        print("ComputerJi Wins.")
    print("Do you want to play again? (Y/N)")
    ans = input()

    if ans == 'n' or ans == 'N':
        break
print("\nThanks for playing along.")
