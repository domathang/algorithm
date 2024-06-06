ipv6 = input()
n = ipv6.split(":")
# print(n)
if len(n) < 8:
    for i in range(len(n)):
        if n[i] == '':
            for j in range(8 - len(n)):
                n.insert(i, '')
            break
elif len(n) > 8:
    n.remove('')
for i in range(8):
    n[i] = '0' * (4-len(n[i])) + n[i]
print(":".join(n[:8]))