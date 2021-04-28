def solution(prices):
    answer = [0]*len(prices)
    stack = []
    
    for index, value in enumerate(prices):
        while stack and value < prices[stack[-1]]:
            s_index = stack.pop()
            answer[s_index] = index - s_index 
            
        stack.append(index)
    
    while stack:
        s_index = stack.pop()
        answer[s_index] = len(prices) - s_index - 1
    
    return answer
