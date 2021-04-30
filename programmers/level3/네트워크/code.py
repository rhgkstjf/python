from collections import deque

def solution(n, computers):
    answer = 0
    
    visited = [0]*n
    stack = deque()
    stack.append(0)
    
    while stack:
        net_num= stack.popleft()
        network = computers[net_num]
        for conn_index, conn in enumerate(network):
            #print(conn_index)
            if conn == 1:
                if conn_index != net_num and visited[conn_index] == 0:
                    visited[conn_index] = 1
                    #print('{0}번 네트워크 방문'.format(conn_index))
                    stack.append(conn_index)
                    
    lastnum = visited[0]
    for i in visited[1:]:
        if i == 0:
            answer += 1
            if lastnum == 1:
                answer += 1
        lastnum = i
        
    if lastnum == 1:
        answer += 1

    
    return answer
