'''
def solution(numbers):
    
    numbers = list(map(str, numbers))
    answer = ''

    numbers.sort(key=lambda x: (x*4)[:4], reverse = True)
    
    if numbers[0] == "0":
        return "0"
    else:
        for i in numbers:
            answer = answer + i
    
    
    return answer

'''

import functools

def comparator(a, b):
    if a + b > b + a:
        return -1
    if a + b < b + a:
        return 1
    return 0

def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=functools.cmp_to_key(comparator))

    if numbers[0] == '0':
        return '0'

    return ''.join(numbers)
                   