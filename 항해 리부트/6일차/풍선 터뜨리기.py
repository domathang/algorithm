n = int(input())
b = list(map(int, input().split()))
index = [i for i in range(1, n + 1)]
start_idx = 0
move = b.pop(start_idx)
answer = []
answer.append(index.pop(start_idx))

while b:
    if move < 0:
        start_idx = (start_idx + move) % len(b)
    else:
        start_idx = (start_idx + move - 1) % len(b)
    move = b.pop(start_idx)
    answer.append(index.pop(start_idx))
print(*answer)

# from collections import deque
# n = int(input())
# q = deque(enumerate(map(int,input().split())))
# ans=[]

# while q:
#     idx,num = q.popleft()
#     ans.append(idx+1)
#     if num>0:
#         q.rotate(-(num-1))
#     elif num<0:
#         q.rotate(-num)
# print(' '.join(map(str,ans)))
