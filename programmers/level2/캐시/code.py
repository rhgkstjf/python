from collections import deque
def solution(cacheSize, cities):
    answer = 0
    
    que = deque()
    que_size = 0
    
    for i in cities:
        print(que)
        i = i.upper()
        if que and i in que:
            answer += 1
        else:
            if que_size < cacheSize or not que:
                que.append(i)
                que_size += 1
            else:
                que.popleft()
                que.append(i)
                
            answer += 5
    
    return answer
