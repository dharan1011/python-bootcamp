arr = [5,4,1,2,3,4,5,7,8,3]
max(arr)
min(arr)
sorted(arr)
reversed(arr)
reversed(sorted(arr))
sum(arr)

int(1.0)
int('1')
1 -> str(1)
  -> 1 + ""

len(arr)


# Find the average
arr = [.......]
sum(arr)/len(arr)


# Finding meadin
ar  = [1,3,4,5,6,8,2]
n = len(ar)
ar = sorted(ar)
n = 6
if(n % 2 == 0):
    (ar[n / 2] + arr[n / 2 - 1]) / 2
else:
    ar[n / 2]

# https://www.hackerrank.com/challenges/capitalize/problem
def solve(s):
    return " ".join([w.capitalize() for w in s.split(" ")])

