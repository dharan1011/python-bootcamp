# Given a string check if it is palindrome or not

"""
Example

madam -> true
abba -> true
abcd -> false

"""

word = input()
n = len(word)
flag = True
for i in range(0, n):
    last_index = (i + 1) * -1
    if(word[i] != word[last_index]):
        flag = False
        break

if flag:
    print("Its is palindrome")
else:
    print("Not a palindrome")

# Approach 2
word = input()
n = len(word)
reversed_word = "" # store a empty string
for idx in range(n-1, -1, -1): # iterate from reverse
    reversed_word += word[idx]

if(word == reversed_word):
    print("Palindrome")
else:
    print("Not a palindrome")

"""
explanation
word = wine
r_word = ""

idx = 3
r_word = r_word + word[3] -> "" + "e"
r_word = "e"

idx = 2
r_word = r_word + word[2] -> "e" + "n" -> "en"
r_word = "en

idx = 1
r_word = r_word + word[1] -> "en" + "i"
r_word = "eni"

.
.
.
"""

# Approach 3
word = input()
lo = 0
hi = len(word) - 1
flag = True
while lo < hi:
    if(word[lo] != word[hi]):
        flag = False
        break
    lo+=1
    hi-=1
if flag:
    print("Its is palindrome")
else:
    print("Not a palindrome")

x