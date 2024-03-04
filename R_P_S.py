import random

def is_win(player,Ai):
    if (player == 'r' and Ai == 's') or (player == 's' and Ai == 'p')\
        or (player == 'p' and Ai == 'r'):
        return True
def play():
    user = input("r, for rock:  s, for scissors: p, for paper")
    computer = random.choice(['r','p','s']) 
    
    if user == computer:
        return'tie'
    if is_win(user,computer):
        return 'You win'

    return 'You lose'
    

    
print(play())