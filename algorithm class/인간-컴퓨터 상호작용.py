s = input()
q = int(input())
arr = []
for _ in range(q):
    i = input().split()
    arr.append((i[0], int(i[1]), int(i[2])))

alphabet = [[0 for j in range(26)] for i in range(len(s))]

for i in range(len(s)):
    for j in range(26):
        if i != 0:
            alphabet[i][j] += alphabet[i-1][j]
    alphabet[i][ord(s[i]) - ord('a')] += 1

for a, l, r in arr:
    index = ord(a) - ord('a')
    answer = alphabet[r][index]
    if l >= 1:
        answer -= alphabet[l-1][index]
    print(answer)
