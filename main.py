import random

choices = ['Rock','Paper','Scissor']
computer = random.choice(choices)
player = False
cpu_score = 0
player_score=0

while True:
    player = input("Choose Rock, Paper or Scissor: ").capitalize()
    if player == computer:
        print("\tYou and Computer chose the same. It's a Tie!")
    elif player == 'Rock':
        if computer == 'Paper':
            print("\tPlayer:",player)
            print("\tComputer:",computer)
            print("\tYou lose!",computer,"covers",player)
            cpu_score+=1
        else:
            print("\tPlayer:",player)
            print("\tComputer:",computer)
            print("\tYou win!",player,"smashes",computer)
            player_score+=1
    elif player == 'Paper':
        if computer == 'Scissor':
            print("\tPlayer:",player)
            print("\tComputer:",computer)
            print ("\tYou lose!",computer,"cuts",player)
            cpu_score+=1
        else:
            print("\tPlayer:",player)
            print("\tComputer:",computer)
            print("\tYou win!",player,"covers",computer)
            player_score+=1
    elif player == 'Scissor':
        if computer == 'Rock':
            print("\tPlayer:",player)
            print("\tComputer:",computer)
            print ("\tYou lose!",computer,"smashes",player)
            cpu_score+=1
        else:
            print("\tPlayer:",player)
            print("\tComputer:",computer)
            print("\tYou win!",player,"cuts",computer)
            player_score+=1

    elif player=='End':
        print("Final Scores:")
        print(f"\tComputer:{cpu_score}")
        print(f"\tPlayer:{player_score}")
        break

