def solution(n, lost, reserve):
    answer = 0
    
    arr = [1]*n
    for i in lost:
        arr[i-1] -= 1
    for i in reserve:
        arr[i-1] += 1
    for i in range(n):
        if arr[i] > 1:
            if i > 0 and arr[i-1] < 1:
                arr[i-1] += 1
            elif i+1 < n and arr[i+1] < 1:
                arr[i+1] += 1
            arr[i] -= 1
        
    for i in arr:
        if i != 0:
            answer += 1
        
    return answer
