s = input()
answer = 0
i = 0
while i < len(s):
    cro = s[i:i+2]
    if cro == "c=" or cro == 'c-' or cro == "d-" or cro == 'lj' or cro == "nj" or cro == "s=" or cro == "z=":
        i += 1
    elif i <= len(s)-3 and s[i:i+3] == "dz=":
        i += 2
    answer += 1
    i += 1
print(answer)