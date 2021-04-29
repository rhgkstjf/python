def solution(a, b):
    answer = 0
    for index, value in enumerate(a):
        answer += value*b[index]
    return answer
