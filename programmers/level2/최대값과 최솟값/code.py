def solution(s):
    
    s = list(map(int, s.split(' ')))
            
    #print(s)
    return '{0} {1}'.format(min(s),max(s))
