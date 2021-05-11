def solution(n, words):
    answer = [0,0]
    
    save = []
    
    previos = ''
    for index, i in enumerate(words):
        if save and i in save:
            answer[0] = ((index%n)+1)
            answer[1] = (int((index/n)+1))
            break
            
        else:
            if previos == '':
                save.append(i)
                previos = i[-1]
            elif previos == i[0]:
                save.append(i)
                previos = i[-1]
            else:
                answer[0] = ((index%n)+1)
                answer[1] = (int((index/n)+1))
                break

    return answer
