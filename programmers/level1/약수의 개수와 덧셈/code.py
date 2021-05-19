def judge(value):
    flag = 0
    for i in range(1,value+1):
        if value%i == 0:
            flag += 1
            
    return flag

def solution(left, right):
    answer = 0
    
    for i in range(left,right+1):
        if judge(i)%2 == 0:
            answer += i
        else:
            answer -= i
            
    return answer
