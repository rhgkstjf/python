from datetime import date
def solution(a, b):
    answer = ''

    d = date(2016, a, b)
    answer = d.ctime().split(' ')[0].upper()
    
    return answer
