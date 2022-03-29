def binary_search(arr, target):
    l = 0
    r = len(arr) - 1
    m = (l + r) // 2

    arr.sort()

    while l <= r:
        print(l, r, m)
        if arr[m] < target:
            l = m + 1
        elif arr[m] > target:
            r = m - 1
        else:
            return arr, m
        m = (l + r) // 2

    return arr, -1


print(binary_search([1, 5, 4, 3, 7, 9, 8, 30, 20], 30))
