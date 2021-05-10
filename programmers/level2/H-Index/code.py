def solution(citations):
    answer = 0
    
    citations.sort(reverse=True)
    print(citations)
    for index,value in enumerate(citations):
        if index < value:
            answer = index+1
    
    return answer
