s = input()
answer = []
for i in range(1, len(s) - 1):
    for j in range(i + 1, len(s)):
        a, b, c = s[:i][::-1], s[i:j][::-1], s[j:][::-1]
        new_s = a + b + c
        answer.append(new_s)
answer.sort()
print(answer[0])
