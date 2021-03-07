# scanning user input to list
nums = []
n = int(input())
for i in range(0, n):
    x = int(input())
    nums.append(x)


# defining function
# def function_name(input):
#   code  here

def find_max(nums):
    res = nums[0]
    for i in range(1, len(nums)):
        res = max(res, nums[i])
    return res