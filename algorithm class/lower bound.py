def lower_bound(n, arr, k):
    l = 0
    r = n - 1
    m = (l + r) // 2

    while l < r:
        if arr[m] < k:
            l = m + 1
        elif arr[m] >= k:
            r = m
        m = (l + r) // 2
    return l + 1

print(lower_bound(7, [1, 2, 2, 2, 2, 2, 3], 2))
