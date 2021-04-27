#answers = [1,3,2,4,2]
answers = [1,2,3,4,5]
def solution(answers):
    answer = []
    
    user_1 = [1,2,3,4,5]
    user_2 = [2,1,2,3,2,4,2,5]
    user_3 = [3,3,1,1,2,2,4,4,5,5]
    
    user_1_check = 0
    user_2_check = 0
    user_3_check = 0
    
    for index,value in enumerate(answers):
        if value == user_1[index%5]:
            user_1_check += 1
            
        if value == user_2[index%8]:
            user_2_check += 1
            
        if value == user_3[index%10]:
            user_3_check += 1


    virtual_answer = [user_1_check,user_2_check,user_3_check]
    for user, value in enumerate(virtual_answer):
        if value == max(virtual_answer):
            answer.append(user+1)
            
        
    
    return answer

print(solution(answers))
