import re

def transform(strr):
    jcd = []
    s_size = len(strr)
    for i in range(s_size-1):
        ch_1 = strr[i]
        ch_2 = strr[i+1]
        jcd.append((ch_1+ch_2))

    return jcd
    
def solution(str1, str2):
    answer = 0
    
    p = re.compile('[a-zA-Z]+')
    str1 = ''.join(p.findall(str1)).upper()
    str2 = ''.join(p.findall(str2)).upper()
    
    jcd1 = transform(str1)
    jcd2 = transform(str2)
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
