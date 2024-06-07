n = int(input())
sg = {*list(map(int,input().split()))}
m = int(input())
js = list(map(int,input().split()))
print(*[1 if i in sg else 0 for i in js])