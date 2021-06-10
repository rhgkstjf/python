def solution(arr):
    answer = []
    if len(arr) == 1:
        answer = [-1]
        
    else:
        tmp = sorted(arr,reverse=True);
        item = tmp[-1]
        
        arr.remove(item)
        answer = arr
    return answer
