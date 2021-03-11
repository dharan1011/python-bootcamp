# Given a string. Reverse the string and print it
"""
Example : 
Vinay -> yaniV

dharan -> 6

0 1 2 3 4 5
d h a r a n
"""

word = input() # wine
n = len(word) # 4
for idx in range(n - 1, -1, -1):
    print(word[idx], end='')
print()
# for idx in range(0, n, 1):
#     print(word[idx], end='')