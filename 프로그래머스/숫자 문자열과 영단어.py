def solution(s):
    answer = ''
    eng_words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    while len(s) > 0:
        for i in range(len(eng_words)):
            if s.startswith(eng_words[i]):
                answer += str(eng_words.index(eng_words[i]))
                s = s[len(eng_words[i])::]
                print(s)
            if s.startswith(str(i)):
                answer += str(i)
                s = s[1::]
                print(s)
    return int(answer)


print(solution("one4seveneight"))
