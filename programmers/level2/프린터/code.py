def solution(priorities, location):
    answer = 0
    stack = []
    flag = True
    for i in range(len(priorities)):
        stack.append(i+1)

    while stack:
        flag = True
        p_id = stack.pop(0)

        for prio in priorities:
            if priorities[p_id-1] < prio:
                stack.append(p_id)
                flag = False
                break
                
        if flag:
            priorities[p_id-1] = 0
            answer += 1
            if p_id-1 == location:
                break

    return answer
