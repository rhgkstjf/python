def solution(s):
    answer = []
    
    Data = s[2:-2]
    Data = Data.split('},{')
    Data = sorted(Data, key = lambda x: len(x))
    
    for i in Data:
        v_list = i.split(',')
        for j in v_list:
            if int(j) not in answer:
                answer.append(int(j))
    
    
    return answer
