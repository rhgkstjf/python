def solution(N, stages):
    answer = []
    
    clear_fail = {}
    for i in stages:
        if i <= N:
            clear_fail[i] = clear_fail.get(i,0) + 1
    
    user_num = len(stages)
    clear_fail_per = [0]*N
    for i in range(1,N+1):
        if clear_fail.get(i) is not None:
            clear_fail_per[i-1] = clear_fail[i]/user_num
            user_num -= clear_fail[i]
    
    
    for index, per in enumerate(clear_fail_per):
        clear_fail[index+1] = per
        
    #print(clear_fail)
    final_data = sorted(clear_fail.items(), key=lambda x: (-x[1], x[0]))
    for index,_ in final_data:
        answer.append(index)
    
    
    return answer
