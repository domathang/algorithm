def upper_bound(n, arr, k):
    l = 0
    r = n - 1
    m = (l + r) // 2

    if arr[-1] < k:
        return n + 1

    while l < r:
        if arr[m] <= k:
            l = m + 1
        elif arr[m] > k:
            r = m
        m = (l + r) // 2
    return l + 1

print(upper_bound(5, [1,2,3,4,5], 7))
