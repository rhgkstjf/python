def solution(progresses, speeds):
    answer = []
    
    pop_num = 0
    
    while progresses:
        
        for index, value in enumerate(progresses):
            progresses[index] += speeds[index]
            if progresses[index] > 99 and index == pop_num:
                pop_num += 1
        
        for i in range(pop_num):
            progresses.pop(0)
            speeds.pop(0)
        
        if pop_num > 0:
            answer.append(pop_num)
            pop_num = 0
                
    return answer
