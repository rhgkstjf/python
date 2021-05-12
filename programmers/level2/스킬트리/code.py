def solution(skill, skill_trees):
    answer = 0
    skill_size = len(skill)
    tree_size = len(skill_trees)
    order = 0
    
    for i in skill_trees:
        print(len(i), ' str : ', i)
        for j in range(len(i)):
            if i[j] in skill:
                if i[j] != skill[order] and order < skill_size:
                    answer += 1
                    break
                else:
                    order += 1
                  
        order = 0
    
    
    return tree_size-answer
