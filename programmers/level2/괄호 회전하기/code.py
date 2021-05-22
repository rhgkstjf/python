def check(s):
    stack = []
    for i in s:
        if i in ['(','{','[']:
            stack.append(i)
        elif stack:
            if stack[-1] == '(' and i == ')':
                stack.pop()
            elif stack[-1] == '{' and i == '}':
                stack.pop()
            elif stack[-1] == '[' and i == ']':
                stack.pop()
            else:
                return 0
        else:
            return 0
        
    if stack:
        return 0
    else:
        return 1

def solution(s):
    answer = 0
    
    for i in range(len(s)):
        answer += check(s)
        s = s[1:] + s[0]
        #print(s)
    #print(check(s))
    
    return answer
