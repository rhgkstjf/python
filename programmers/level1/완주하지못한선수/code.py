def solution(participant, completion):
    answer = ''
    
    participant.sort()
    completion.sort()

    size_c = len(completion)
    
    for i in range(size_c):
        if participant[i] != completion[i]:
            answer = participant[i]
            return answer
        
    answer = participant[size_c]
    return answer
