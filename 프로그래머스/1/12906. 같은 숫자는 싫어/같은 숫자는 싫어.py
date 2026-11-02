def solution(arr):
    stack = []
    answer = []
    for i in arr:
        if  len(stack) == 0 or i == stack[-1]:
            stack.append(i)
        else:
            answer.append(stack[-1])
            stack = []
            stack.append(i)
    answer.append(arr[-1])
    return answer