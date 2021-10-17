import random

pick,options = 'rock',['rock','paper','scissors']

def _get_user_pick():
    
    shot =input('rock, paper, scissors shoot \n >>>')
    
    return shot

def _get_computer_pick():
    
    n = random.random()
    
    index =round(n*3)
    
    comp_pick = options[index]
    
    return comp_pick

def _start_game():
    
    print('rock paper scissors shoot ! \n')
    
    user = _get_user_pick()
    Ai = _get_computer_pick()
    
    if user == 'rock' and Ai == 'scissors':
        print('Computer picked Scissors you won')
    elif user == 'scissors' and Ai == 'paper':
        print('Computer picked paper you won')
    elif user == 'paper' and Ai == 'rock':
        print('Computer picked rock you won')
    elif user == Ai :
        print(f'Computer picked {user} too, so it is a tie')
    else:
        print(f'Sorry you lost, computer picked {Ai}')
    

_start_game()
