"""

n = 3

xxx
x x
xxx

n = 5
xxxxx
x   x
x   x
x   x
xxxxx
"""

def straightLine(n):
    for i in range(n):
        print('*', end = '')
    print()

def hollowLine(n):
    print('*', end = '')
    for i in range(n-2):
        print(' ', end = '')
    print('*')

n = int(input())
straightLine(n)
for i in range(n-2):
    hollowLine(n)
straightLine(n)


        