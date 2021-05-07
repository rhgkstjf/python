def find_points(points,value):
    for index, lst in enumerate(points):
        if value in lst:
            point = [index,lst.index(value)]
            return point

def distance_evl(d1,d2):
    result = abs(d1[0]-d2[0])+abs(d1[1]-d2[1])
    print('d1 : {0} , d2 : {1} ,result = {2}'.format(d1,d2,result))
    return result
    
def solution(numbers, hand):
    answer = ''
    
    points = [[1,2,3],[4,5,6],[7,8,9],['*',0,'#']]
    
    left = [3,0]
    right = [3,2]
    
    for i in numbers:
        if i in [2,5,8,0]:
            i_points = find_points(points,i)
            print('{0} 번호의 좌표값 : {1}'.format(i,i_points))
            distance_l = distance_evl(left,i_points)
            distance_r = distance_evl(right,i_points)
            print('{0} 번호 누르기 위해 계산한 거리 결과 left:{1} , right:{2}'.format(i,distance_l,distance_r))
            if distance_l > distance_r:
                answer += 'R'
                right = i_points
            elif distance_l < distance_r:
                answer += 'L'
                left = i_points
            elif distance_l == distance_r and hand == 'right':
                answer += 'R'
                right = i_points
            else:
                answer += 'L'
                left = i_points
        
        elif i%3 == 1:
            answer += 'L'
            left = [int(i/3),0]
            print('왼손으로 누름 번호 : {0}'.format(i))
        else:
            answer += 'R'
            right = [int(i/3)-1,2]
            print('오른손으로 누름 번호 : {0}'.format(i))
              
    
        
    return answer
