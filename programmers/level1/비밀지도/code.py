def binary_convert(value,arr,n):
    while value > 0:
        if value % 2 == 1:
            arr[n] = 1
        n -= 1
        value = int(value / 2) 
    
def solution(n, arr1, arr2):
    answer = []
    
    for i in range(n):
        tmp_arr = [0]*n
        tmp_ans = ""
        
        binary_convert(arr1[i],tmp_arr,n-1)
        binary_convert(arr2[i],tmp_arr,n-1)
        
        for k in tmp_arr:
            if k == 0:
                tmp_ans += ' '
            else:
                tmp_ans += '#'
        answer.append(tmp_ans)

    return answer
