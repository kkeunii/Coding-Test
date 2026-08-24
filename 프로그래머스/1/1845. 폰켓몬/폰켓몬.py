def solution(nums):
    numbers = set(nums)
    count = len(nums) / 2
    
    if len(numbers) > count:
        answer = count
    else:
        answer = len(numbers)
        
    return answer