from random import randint

def win():
    print ('You win!')

def lose():
    print ('You lose!')
value=True

while value:
    player_choice = input('What do you pick? (rock, paper, scissors)')
    player_choice.strip()
    random_move = randint(0, 2)
    moves = ['rock', 'paper', 'scissors']
    computer_choice = moves[random_move]

    if player_choice ==computer_choice:
        print ('Draw!')
        valu=False
    elif player_choice == 'rock' and computer_choice == 'scissors':
        print(computer_choice)
        win()
        
    elif player_choice  == 'paper' and computer_choice == 'scissors':
        lose()

    elif player_choice == 'scissors' and computer_choice == 'paper':
        print(computer_choice)
        win()
    elif player_choice == 'scissors' and computer_choice == 'rock':
        print(computer_choice)
        lose()
    elif player_choice == "paper" and computer_choice == 'rock':
        print(computer_choice)
        win()
    elif player_choice == "paper" and computer_choice =="rock" :
        print(computer_choice)
        lose()
    aGain = input('Do you want to play again? (y or n)').strip()
    if aGain == 'y':
        value=True
    else:
        value=False

