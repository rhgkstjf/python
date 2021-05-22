def solution(n):
    answer = 0
    
    convert_num = []
    
    while n > 0:
        c_num = n%3
        convert_num.append(c_num)
        n = int(n/3)
    
    index = len(convert_num)-1
    for i in convert_num:
        answer += 3**index * i
        index -= 1
        
    
    return answer
