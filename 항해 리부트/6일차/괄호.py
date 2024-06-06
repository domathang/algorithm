n = int(input())
for i in range(n):
    brac = input()
    f = 0
    for j in brac:
        if j == "(":
            f += 1
        elif j == ")":
            if f == 0:
                f = -1
                break
            f -= 1
    if f == 0:
        print("YES")
    else:
        print("NO")