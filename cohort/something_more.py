# List Comprehensions
# ADD 1 to 100 in list
arr = []
for i in range(1,101):
    arr.append(i)


arr = [i for i in range(1,101)]

# Add square of 1 to 25

arr = []
for i in range(1,26):
    arr.append(i*i)

arr = [i*i for i in range(1,26)]


def print_matrix(mat):
    rows = len(mat)
    cols = len(mat[0])
    for r in range(rows):
        for c in range(cols):
            print(mat[r][c], end=" ")
        print()

mat = [[j for j in range(1,4)] for i in range(3)]
print_matrix(mat)



