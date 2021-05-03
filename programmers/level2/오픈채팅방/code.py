def solution(record):
    answer = []
    result = []
    table = {}
    
    for i in record:
        Data = i.split(' ')
        log = Data[0]
        uid = Data[1]
        
        if log == 'Leave':
            answer.append(uid+' Leave')
        elif log == 'Enter':
            name = Data[2]
            table[uid] = name
            answer.append(uid+' Enter')
        else:
            name = Data[2]
            table[uid] = name

    for i in answer:
        Data = i.split(' ')
        name = table[Data[0]]
        log = Data[1]
        
        if log == 'Enter':
            result.append('{0}님이 들어왔습니다.'.format(name))
        else:
            result.append('{0}님이 나갔습니다.'.format(name))

    return result
