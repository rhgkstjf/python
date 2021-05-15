from collections import deque
def solution(cacheSize, cities):
    answer = 0
    
    que = deque()
    que_size = 0
    
    #테스트 케이스 7 17에서 통과하지못했다.
    #이유는 캐시가 사이즈 0일 때에는 캐시 도시를 담지 못하므로 무조건miss가 일어나기 때문에, 밑에와 같은 연산을 거칠 필요가없었다.
    #시간 때문에 통과를 못한 것 같다.
    if cacheSize == 0:
        return len(cities)*5
    
    for i in cities:
        i = i.upper()
        if que and i in que:
            answer += 1
            que.remove(i)
            que.append(i)
        else:
            if que_size < cacheSize or not que:
                que.append(i)
                que_size += 1
            else:
                que.popleft()
                que.append(i)
                
            answer += 5
    
    return answer
