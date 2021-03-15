# Print multiplication table of number from 1 to 10 upto 10 in each table

"""

[]
sorted | un-sorted

1 2 3 5 7 9

"""

def selection_sort(numbers_list):
    n = len(numbers_list)
    for i in range(0,n): 
        # ith idx
        min_idx = i
        # [0...i-1 | i...n]
        for j in range(i, n):
            if(numbers_list[j] < numbers_list[min_idx]):
                min_idx = j
        numbers_list[min_idx], numbers_list[i] = numbers_list[i], numbers_list[min_idx]


def selection_sort(numbers_list):
    n = len(numbers_list)
    for i in range(1, n):
        key = numbers_list[i]
        j = i - 1
        while(j >= 0 and numbers_list[j] > key):
            numbers_list[j+1] = numbers_list[j]
        numbers_list[j+1] = key

nums = [7,8,1,2,4,5]
selection_sort(nums)
print(nums)

"""


1,8,7,2,4,5

i = 0
min_idx = 0

j = 0
if(7 < 7)
j = 1
if(8 < 7)
j = 2
if(1 < 7):
    min_idx = 2
j = 3
if(2 < 1):

if(2 != 0):
    
"""




