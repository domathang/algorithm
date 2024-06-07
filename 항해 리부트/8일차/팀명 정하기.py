lst = []
for i in range(3):
    score, year, name = input().split()
    lst.append((int(score), int(year) % 100, name[0]))
lst.sort(key=lambda x: x[1])
print(*[i[1] for i in lst], sep="")
lst.sort(key=lambda x: x[0], reverse=True)
print(*[i[2] for i in lst], sep="")
