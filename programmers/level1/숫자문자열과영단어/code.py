def solution(s):
    answer = []
    
    num_dict = {
        'zero' : '0',
        'one' : '1',
        'two' : '2',
        'three' : '3',
        'four' : '4',
        'five' : '5',
        'six' : '6',
        'seven' : '7',
        'eight' : '8',
        'nine' : '9'
    }
    
    prefix = ''
    
    for i in s:
        if i.isdigit():
            answer.append(i)
            
        else:
            prefix += i
            if prefix in num_dict:
                answer.append(num_dict[prefix])
                prefix = ''

    return int(''.join(answer))
