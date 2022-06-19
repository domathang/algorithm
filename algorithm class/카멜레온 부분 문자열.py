s = input()

if len(s) == 1:
    print(-1)

else:
    s1 = s[:-1]
    s2 = s[1:]
    for i in range(len(s2)):
        cur1 = 0
        cur2 = i
        flag = False
        while s1[cur1] == s2[cur2]:
            cur1 += 1
            cur2 += 1
            if cur2 == len(s2):
                same_s = s[:cur1]
                part_s = s[1:-1]
                if part_s.find(same_s) != -1:
                    print(same_s)
                    flag = True
                break
        if flag:
            break
        elif i == len(s2) - 1:
            print(-1)
