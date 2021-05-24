def solution(x):
    answer = True
    sum = 0
    tmp_x= str(x)
    for i in tmp_x:
        sum += int(i)
    
    if x%sum != 0:
        answer = False
    
    return answer
