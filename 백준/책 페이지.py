n = int(input())

arr = [0] * 10

for digit in range(len(str(n))):

    if len(str(n)) == 1:
        for k in range(1, n+1):
            arr[k] += 1
        continue

    other_numbers = ''
    for k in range(len(str(n))):
        if k != digit:
            other_numbers += str(n)[k]
    other_numbers = int(other_numbers)
    x = 10 ** (len(str(n)) - digit - 1)
    up_other_numbers = (other_numbers + x) - (other_numbers % x)
    down_other_numbers = other_numbers - (other_numbers % x)
    down_down_other_numbers = down_other_numbers - x

    for k in range(10):
        if digit == 0:  # 제일 큰 자릿수일 때
            if k != 0:
                if k < int(str(n)[0]):
                    arr[k] += 10 ** (len(str(n)) - 1)
                elif k == int(str(n)[0]):
                    arr[k] += other_numbers + 1

        elif digit == len(str(n)) - 1:  # 마지막 자릿수일 때
            if int(str(n)[digit]) == 0 or k == 0 or k > int(str(n)[digit]):
                arr[k] += other_numbers
            else:
                arr[k] += other_numbers + 1
        else:
            if int(str(n)[digit]) != 0:
                if k == 0:
                    arr[k] += down_other_numbers
                elif k < int(str(n)[digit]):
                    arr[k] += up_other_numbers
                elif k == int(str(n)[digit]):
                    arr[k] += other_numbers + 1
                elif k > int(str(n)[digit]):
                    arr[k] += down_other_numbers
            else:
                if k != 0:
                    arr[k] += down_other_numbers
                else:
                    arr[k] += down_down_other_numbers + (n % x) + 1


arr = [str(i) for i in arr]
print(' '.join(arr))
