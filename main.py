import random

choices = ['Rock','Paper','Scissor']
computer = random.choice(choices)
player = False
cpu_score = 0
player_score=0

while True:
    player = input("Choose Rock, Paper or Scissor").capitalize()
    if player == computer:
        print("You and Computer chose the same. It's a Tie!")
    elif player == 'Rock':
        if computer == 'Paper':
            print("You lose!",computer,"covers",player)
            cpu_score+=1
        else:
            print("You win!",player,"smashes",computer)
            player_score+=1
    elif player == 'Paper':
        if computer == 'Scissor':
            print ("You lose!",computer,"cuts",player)
            cpu_score+=1
        else:
            print("You win!",player,"covers",computer)
            player_score+=1
    elif player == 'Scissor':
        if computer == 'Rock':
            print ("You lose!",computer,"smashes",player)
            cpu_score+=1
        else:
            print("You win!",player,"cuts",computer)
            player_score+=1

    elif player=='End':
        print("Final Scores:")
        print(f"CPU:{cpu_score}")
        print(f"Plaer:{player_score}")
        break

