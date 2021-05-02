def solution(absolutes, signs):
    answer = 0
    
    for index,value in enumerate(absolutes):
        if signs[index] == True:
            answer += value
        else:
            answer -= value
    
    return answer
