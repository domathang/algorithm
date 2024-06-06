n = int(input())
m = int(input())
s = input()
lst = []
i= 0
cnt = 0
answer = 0

while i < len(s)-2:
    if s[i:i+3] == "IOI":
        i+=1
        cnt+=1
    elif cnt > 0:
        lst.append(cnt)
        cnt = 0
    i += 1

if cnt > 0:
    lst.append(cnt)
    
for i in lst:
    if i >= n:
        answer += i - n + 1
print(answer)