math_ex = input().split('-')
ans = 0
add_first = 0
for i in math_ex:
    plus_list = i.split('+')
    sum = 0
    if len(plus_list) > 1:
        for j in plus_list:
            sum += int(j)
    else:
        sum = int(plus_list[0])
    ans -= sum
    if i == math_ex[0]:
        add_first = sum
print(ans + add_first*2)
