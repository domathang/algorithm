n = int(input())
lst = set()
cnt = 0
for i in range(n):
    chat = input()
    if chat != "ENTER" and chat not in lst:
        lst.add(chat)
        cnt += 1
    elif chat == "ENTER":
        lst.clear()
print(cnt)