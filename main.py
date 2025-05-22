import random

print('WELCOME TO TICTACTOE...')
print('YOU ARE X')

print('TS IS THE PLAYING BOARD')

print('  A B C ')
print('1|_|_|_|')
print('2|_|_|_|')
print('3|_|_|_|')

combs = 'a1', 'b1', 'c1', 'a2', 'b2', 'c2', 'a3', 'b3', 'c3'

computer = random.choice(combs)

print('Your turn first')

player = input('now where do you want to put your X at? Ex. a1>')

