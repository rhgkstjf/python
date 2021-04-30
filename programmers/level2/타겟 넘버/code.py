from collections import deque

def solution(numbers, target):
    answer = 0
    
    stack = deque()
    stack.append([0,0])

    while stack:
        sum_value, index = stack.popleft()
        
        if index == len(numbers):
            if sum_value == target:
                answer += 1
        else:
            next_num = numbers[index]
            stack.append([sum_value+next_num,index+1])
            stack.append([sum_value-next_num,index+1])

    return answer
