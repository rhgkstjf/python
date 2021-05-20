def solution(s):
    answer = True
    
    p_num = 0
    y_num = 0
    
    for i in s:
        if i.upper() == 'P':
            p_num += 1
        if i.upper() == 'Y':
            y_num += 1
    if p_num != y_num:
        answer = False
        
    return answer
