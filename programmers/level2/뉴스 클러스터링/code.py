def solution(str1, str2):
    answer = 0
    
    str1_size = len(str1)
    str2_size = len(str2)
    
    jcd1 = []
    jcd2 = []
    
    # 처음 정규식을 이용해서 문자열만 추출하고 계산하려헀다.
    # 하지만 틀린 접근이였다, A+A 일 경우, 내가 정규식으로 했던 방식으로 부분집합을 추리면
    # AA가 나온다, 하지만 해당 문제의 경우 공집합이다, A+ -> 특문이 포함되어있어 제외
    # +A -> 위와 동일하게 제외되어 공집합이된다.
    
    for i in range(str1_size-1):
        strr = ''.join(str1[i]+str1[i+1])
        if strr.isalpha():
            jcd1.append(strr.upper())
    
    for i in range(str2_size-1):
        strr = ''.join(str2[i]+str2[i+1])
        if strr.isalpha():
            jcd2.append(strr.upper())
            
    # 중복이 있을 경우 교집합을 구하는 팁은 해당 링크에 잘 적혀있다.
    # https://stackoverflow.com/questions/3697432/how-to-find-list-intersection
    # 작은 리스트의 원소 중 중복된 값을 큰 리스트에서 제외시킨다.
    
    if len(jcd1) > len(jcd2):
        intersect = [jcd1.remove(x) for x in jcd2 if x in jcd1]
    else:
        intersect = [jcd2.remove(x) for x in jcd1 if x in jcd2]
    
    union_set = jcd1+jcd2
    union_size = len(union_set)
    
    if union_size == 0:
        return 65536
    
    answer = int(( len(intersect) / union_size) * 65536)
    
    return answer
