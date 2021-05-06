def solution(d, budget):
    answer = 0
    
    sum_val = 0
    
    d.sort()
    print(d)
    for index, value in enumerate(d):
        sum_val += value
        
        if sum_val <= budget:
            answer += 1
        
        else:
            break

            
    
    
    return answer
