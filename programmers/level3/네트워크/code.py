from collections import deque
    
def solution(n, computers):
    answer = 0
    
    visited = [0]*n
    queue = deque()
    
    while 0 in visited:
        not_clear = visited.index(0)
        queue.append(not_clear)
        visited[not_clear] = 1
        while queue:
            network_num = queue.popleft()
            for i in range(n):
                if visited[i] == 0 and computers[network_num][i] == 1:
                    queue.append(i)
                    visited[i] = 1
        answer += 1
        
    return answer
