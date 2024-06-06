n = int(input())
q = {}
lst = []
answer = 0

for i in range(n):
    q[input()] = i

for i in range(n):
    number = input()
    lst.append(q[number])

for i in range(n):
    for j in range(i, n):
        if lst[i] > lst[j]:
            answer += 1
            break
print(answer)
