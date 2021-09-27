def solution(record):
    command = []
    uid = []
    nickname = []
    ans = []
    dic = dict()

    for r in record:
        if len(r.split()) == 3:
            c, u, n = r.split(' ')
            dic[u] = n
            command.append(c)
            uid.append(u)
            nickname.append(n)
        else:
            c, u = r.split(' ')
            command.append(c)
            uid.append(u)
            nickname.append('-')

    for i in range(len(record)):
        if command[i] == "Enter":
            ans.append(dic[uid[i]] + "님이 들어왔습니다.")
        elif command[i] == "Leave":
            ans.append(dic[uid[i]] + "님이 나갔습니다.")

    return ans

print(solution(["Enter uid1234 Muzi",
                "Enter uid4567 Prodo",
                "Leave uid1234",
                "Enter uid1234 Prodo",
                "Change uid4567 Ryan"]))
