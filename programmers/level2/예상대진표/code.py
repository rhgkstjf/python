def solution(n,a,b):
    answer = 0

    while n>1:
        answer += 1
        if (a%2 == 0 and b == a-1) or (b%2 == 0 and a == b-1):
            break
        else:
            a = (a+1)//2
            b = (b+1)//2
            
            n = n/2

    return answer
