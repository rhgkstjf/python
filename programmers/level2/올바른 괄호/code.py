def solution(s):
    answer = True
    
    stack = []
    
    for i in s:
        if i == ')' and not stack:
            return False
        elif i == ')' and stack:
            stack.pop()
        elif i == '(':
            stack.append(i)
    
    if stack:
        return False
    
    return True
