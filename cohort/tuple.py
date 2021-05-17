x = 1
y = 3
z = 5

100 ?

points = [[1,2,3],[5,6,6],[1,4,8],.....] # read/write -> mutable
for p in points:
    x = p[0]
    y = p[1]
    z = [2]
    # Logic

points = [(1,2,3),(4,5,7),(3,6,8)....] # read -> immutable
for p in points:
    x,y,z = p

def solve(person_info):
    first_name, last_name, age, sex, rs = person_info
    # Logic

person_info = ("Vinay","Karka",24,"Male","Single")
solve(person_info)

def solve(arr):
    return (min(arr), max(arr))

1,2,3
4,5,6
7,8,9

n x m

2 x 4

1 2 3 4
5 6 7 8

n,m

mat = []
cnt = 1
for i in range(n):
    row = []
    for j in range(m):
        row.append(cnt)
        cnt += 1
    mat.append(row)

mat -> [[1,2,3,4],[5,6,7,8],[9,10,11,12],.......]

n,m
cnt = 0
def gen():
    cnt = 0
    yield cnt += 1
mat = [[gen() for j in range(m)] for i in range(n)]
