l = int(input())
strr = input()
answer = 0
for i in range(l):
    n = ord(strr[i]) - 96
    answer += n * 31 ** i
print(answer % 1234567891)