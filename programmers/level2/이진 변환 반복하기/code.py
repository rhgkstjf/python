def solution(s):
    answer = []
    
    rotation = 0
    remove_zero = 0
    while len(s) >= 2:
        rotation += 1
        tmp_s = ""
        for i in s:
            if i == '1':
                tmp_s += i
            else:
                remove_zero += 1
        
        b_loof = len(tmp_s)
        b_result = ""
        while b_loof>0:
            b_result += str(b_loof % 2)
            b_loof = b_loof//2
        
        s = b_result[::-1]
        
    answer.append(rotation)
    answer.append(remove_zero) 
        
    
    return answer
