import random

def play():
    user = input('Choose r, p, or s: ').lower()
    comp = random.choice(['r', 'p', 's'])
    
    if user == comp:
        return 'It\'s a tie'
    elif win(user, comp):
        return 'You win'
    else:
        return 'You lost'

def win(a, b):
    return (a == 'r' and b == 's') or (a == 's' and b == 'p') or (a == 'p' and b == 'r')

result = play()
print(result)
