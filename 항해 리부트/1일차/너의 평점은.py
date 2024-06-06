e = {"A+": 4.5, "A0": 4.0, "B+": 3.5, "B0": 3.0, "C+": 2.5, "C0": 2.0, "D+": 1.5, "D0": 1.0, "F": 0}
s1, s2 = 0, 0
for i in range(20):
    s, c, l = input().split()
    c = float(c)
    if l == "P":
        continue
    s1 += c * e[l]
    s2 += c
print(s1 / s2)
