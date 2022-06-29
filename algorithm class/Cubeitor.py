s = input()
answer = 0
for a in range(len(s)):
    pattern = s[a:]
    pi = [0] * len(pattern)
    j = 0
    for i in range(1, len(pattern)):
        while j > 0 and pattern[i] != pattern[j]:
            j = pi[j-1]
        if pattern[i] == pattern[j]:
            j += 1
            pi[i] = j
    if answer < max(pi):
        answer = max(pi)
    print(pi)
print(answer)
