# Take n numbers as input from user and store in a list
"""
6
1 2 3 4 5 6
"""

n = int(input())
nums = []
for i in range(0,n):
    x = int(input())
    nums.append(x)

print(nums)