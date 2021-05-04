def solution(lottos, win_nums):
    answer = []
    
    correct = 0
    zero = 0
    for i in lottos:
        if i in win_nums:
            correct += 1
        elif i == 0:
            zero += 1
    
    print('correct : {0}, zero : {1}'.format(correct,zero))
    
    answer.append(7-max(correct+zero,1))
    answer.append(7-max(correct,1))
    
    
    return answer
