import collections

def solution(participant, completion):
    
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]
    '''
    check = {}
    answer=''
    for i in participant:
        if i in check:
            check[i] += 1
        else:
            check[i] = 1
            
    for i in completion:
        check[i] -= 1
    
    for i in check:
        if check[i] == 1:
            answer = i
    
    
    return answer
'''