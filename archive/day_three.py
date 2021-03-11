"""
    Agenda:
        1. Arrays
"""

#           0       1       2
# names = ["vinay","ajay","srikesh"]
# empty_arr = []

# Write a program to scan 10 names and print "Hello, $names"

num = int(input())
names = []
for i in range(0,num):
    x = input()
    names.append(x)
"""
[]
['A','b','c','d'....]
"""

print(names)

for i in range(0, num):
    print("Hello,", names[i])

"""
Creating a empty array
var_name = [] 
Array can be pre decalred
var_name = [1,2,3,4,5,6]
"""

# Write a program to take n numbers from user and print sum of n numbers

# Write a program to take n numbers from user and print max of n numbers