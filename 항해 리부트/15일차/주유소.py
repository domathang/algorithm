n = int(input())
length = list(map(int, input().split()))
price = list(map(int, input().split()))

answer = 0
min_price = price[0]
for i in range(n-1):
    min_price = min(min_price,price[i])
    answer += min_price * length[i]
print(answer)