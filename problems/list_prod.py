def solve(arr):
    n = len(arr)
    res = []
    for i in range(n):
        left_prod = 1
        right_prod = 1
        for j in range(i):
            left_prod = left_prod * arr[j]
        for j in range(i + 1, n):
            right_prod = right_prod * arr[j]
        res.append(left_prod * right_prod)
    return res