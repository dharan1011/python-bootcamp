"""
Loops are used to iterate over a sequence

Example of sequence :
a,d,i,t,y,a
1,2,3,4,5,6
"Dharan","vinay","Danesh"

Sequence in python
string
list


range(start, end) function is used to generate a sequence of numbers

Note:
in each iteration each element in the sequence is accessed

for counter_variable in [sequence]:
    Code
"""

#Print all character in a string separated by a newline
name = "vinay"
for c in name:
    print(c)

"""
itr = 1
c = v
print(c) -> v

itr = 2
c = i
.
.
.
"""

nums = [1,2,3,4,5,6,7,8]


for x in nums:
    print(x)

# generating indexes of nums using range function
for i in range(0, len(nums)):
    print(nums[i])


"""
Find the sum of all numbers from 1 to 100

x = 1 + 2 + 3 + 4 + 5 + .... + 100
"""
s = 0
for x in range(1,101):
    s += x
print(s)

