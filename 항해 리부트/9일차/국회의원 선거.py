n = int(input())
lst = []
for i in range(n):
    lst.append(int(input()))
answer = 0
dasom = lst[0]
other = lst[1:]
while other and dasom <= max(other):
    idx = other.index(max(other))
    other[idx] -= 1
    dasom += 1
    answer += 1
print(answer)