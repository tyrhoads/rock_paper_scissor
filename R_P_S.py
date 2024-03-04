import random


def is_win(player,Ai):
    if (player == 'r' and Ai == 's') or (player == 's' and Ai == 'p')\
        or (player == 'p' and Ai == 'r'):
        return True
def play():
    user = input("choose your weapon:  r, for rock:  s, for scissors: p, for paper")
    computer = random.choice(['r','p','s']) 
    
    if user == computer:
        return'tie'
    if is_win(user,computer):
        return 'You win'

    return 'You lose'
    
while True:

    print(play())
    question = input("would you like to continue[y/n]")
    if question == 'n':
        break