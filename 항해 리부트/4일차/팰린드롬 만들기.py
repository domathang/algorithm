from collections import Counter

name_counter = Counter(input())
answer = ''
mid = ''

sorted_keys = sorted(list(name_counter.keys()))

for i in sorted_keys:
    if name_counter[i] % 2 == 1:
        if mid != '':
            print("I'm Sorry Hansoo")
            exit(0)
        mid = i
        name_counter[i] -= 1
        
for i in sorted_keys:
    if name_counter[i] > 0:
        answer += i * (name_counter[i] // 2)

print(answer + mid + answer[::-1])