from math import gcd

def gcd(x,y):
    while y != 0:
        x, y = y, x%y
    return x

def solution(n, m):
    answer = []
    
    answer.append(gcd(n,m))
    answer.append(n*m // gcd(n,m))
    
    return answer
