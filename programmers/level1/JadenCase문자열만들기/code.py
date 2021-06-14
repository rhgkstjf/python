def solution(s):
    answer = ''
    p = s.split(' ')
    size = len(p)
    for index,value in enumerate(p):
        answer += value.capitalize()
        if index < size-1:
            answer += ' '

    return answer
