import heapq

def solution(N, road, K):
    answer = 0
    
    dist = [999999]*(N+1)
    PriorityQ = []
    heapq.heappush(PriorityQ, (1,0))
    dist[1] = 0
    
    while PriorityQ:
        cnode, c_weight = heapq.heappop(PriorityQ)
        for start, end, weight in road:
            cost_evl = c_weight + weight
            if start == cnode and cost_evl < dist[end]:
                dist[end] = cost_evl
                heapq.heappush(PriorityQ, (end, cost_evl))
            elif end == cnode and cost_evl < dist[start]:
                dist[start] = cost_evl
                heapq.heappush(PriorityQ, (start, cost_evl))
    
    answer = len([i for i in dist if i <= K])
            
        

    return answer
