def solution(fees, records):
    answer = []
    default_time = fees[0]
    default_fee = fees[1]
    unit_time = fees[2]
    unit_fee = fees[3]

    history = {}
    time_to_pay = {}
    for time, number, io in [i.split() for i in records]:
        time_split = time.split(":")
        minute_time = int(time_split[0]) * 60 + int(time_split[1])
        if io == 'IN':
            history[number] = minute_time
        elif io == 'OUT':
            if number in time_to_pay:
                time_to_pay[number] += minute_time - history.pop(number)
            else:
                time_to_pay[number] = minute_time - history.pop(number)

    # IN만 있고 OUT 이 없을 경우
    for k, v in history.items():
        last_time = (23 * 60 + 59)
        if k in time_to_pay:
            time_to_pay[k] += last_time - history[k]
        else:
            time_to_pay[k] = last_time - history[k]

    # 추가 요금
    for number, time in time_to_pay.items():
        plus_time = 0
        if time > default_time:
            plus_time = (time - default_time) // unit_time
            if (time - default_time) % unit_time != 0:
                plus_time += 1

        answer.append((number, default_fee + plus_time * unit_fee))

    answer.sort(key=lambda x: x[0])

    return [i[1] for i in answer]


print(solution([180, 5000, 10, 600],
               ["05:34 5961 IN",
                "06:00 0000 IN",
                "06:34 0000 OUT",
                "07:59 5961 OUT",
                "07:59 0148 IN",
                "18:59 0000 IN",
                "19:09 0148 OUT",
                "22:59 5961 IN",
                "23:00 5961 OUT"]))