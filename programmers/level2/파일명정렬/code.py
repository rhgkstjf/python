import re
def solution(files):
    answer = []
    re_list = []
    #p = re.compile(r'([^0-9]+|[0-9]+|[\w\W]+)')
    
    #초기 내가 만든 정규식으로 테스트를 해보니 런타임 에러가 발생했다.
    #그냥 숫자를 기준으로 나누어서 리턴된 값 m을 바로 배열에 추가시켰다.
    #저렇게 해보니 런타임 에러가 발생하지않고 잘 되었다.
    
    for k in files:
        m = re.split(r'([0-9]+)',k)
        #m = p.findall(k)
        #print(m)
        #head = m[0]
        #number = m[1]
        #tail = m[2]
        re_list.append(m)
    # 리스트의 값 중 2개 이상의 값을 기준으로 정렬하고 싶을 때 아래와 같이 사용하면 된다.
    re_list = sorted(re_list, key = lambda e :(e[0].upper(), int(e[1])))
    for i in re_list:
        answer.append("".join(i))
    
    return answer
