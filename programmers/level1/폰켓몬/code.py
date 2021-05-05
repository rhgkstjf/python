def solution(nums):
    answer = 0
    size = len(nums)/2
    tmp = set(nums)
    tmp_size = len(tmp)
    
    if tmp_size > size:
        answer = size
    else:
        answer = tmp_size
    
    
    
    return answer
