n, m = map(int, input().split())
ssd = []
for i in range(n):
    ssd.append(int(input()))
l = 0
r = m * min(ssd)
while l < r:
    total = 0
    mid = (l + r) // 2

    for i in ssd:
        total += mid // i

    if total < m:
        l = mid + 1
    elif total >= m:
        r = mid
    
print(l)

# ssd.sort()
# seconds = 0
# for i in range(m):
#     target = ssd.pop(0)
#     seconds = target[0]
#     target = (target[0] + target[1], target[1])
#     s = 0
#     e = len(ssd)-1
#     md = e // 2
#     if len(ssd) == 0 or ssd[e][0] < target[0]:
#         ssd.append(target)
#     elif ssd[s][0] >= target[0]:
#         ssd.insert(0, target)
#     else:
#         while s != md:
#             if ssd[md][0] < target[0] <= ssd[md+1][0]:
#                 ssd.insert(md+1, target)
#                 break
#             elif ssd[md+1][0] < target[0]:
#                 s = md
#             elif ssd[md][0] >= target[0]:
#                 e = md
#             md = (s+e) // 2
#             print(s, md, e)
#         if s == md:
#             ssd.insert(s+1, target)
#     print(ssd)
# print(seconds)
