def prime(num):
    for i in range(2,num):
        if num%i == 0:
            return 0
    
    return 1


def solution(nums):
    answer = 0
    size = len(nums)
    
    for i in range(0,size-2):
        for j in range(i+1,size-1):
            for k in range(j+1,size):
                sum_val = nums[i] + nums[j] + nums[k]
                answer += prime(sum_val)
    
    return answer
