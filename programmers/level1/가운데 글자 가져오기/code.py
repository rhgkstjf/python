def solution(s):
    size = len(s)
    middle = int(size/2)
    if size%2 == 0:
        answer = s[middle-1:middle+1]
    else:
        answer = s[middle]
    
    return answer
