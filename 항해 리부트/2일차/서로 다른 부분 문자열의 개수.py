s = input()
arr = []
for i in range(1, len(s)+1):
    for j in range(len(s)):
        arr.append(s[j:j+i])
print(len(set(arr)))
