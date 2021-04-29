import heapq

def solution(scoville, K):
    answer = 0
    
    heapq.heapify(scoville)
    while True:
        
        answer += 1
        evl = heapq.heappop(scoville) + (heapq.heappop(scoville)*2)
        heapq.heappush(scoville,evl)
        
        if len(scoville) <= 1 and scoville[0] < K:
            answer = -1
            break
        if scoville[0] >= K:
            break
            
    return answer
