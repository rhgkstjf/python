bridge_length = 2
weight = 10
truck_weights = [7,4,5,6]


def solution(bridge_length, weight, truck_weights):
    answer = 0
    queue = [0 for i in range(bridge_length)]

    print(queue)
    while queue:
        queue.pop(0)
        answer = answer + 1
        if truck_weights:
            if sum(queue) + truck_weights[0] <= weight:
                queue.append(truck_weights.pop(0))
            else:
                queue.append(0)
            
    return answer

print(solution(bridge_length,weight,truck_weights))
