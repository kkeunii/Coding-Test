def solution(n, lost, reserve):
    
    check = [1] * (n+2)

    for i in lost:
        check[i] -= 1
        
    for i in reserve:
        check[i] += 1
        
    for i in range(1, n+1):
        if check[i] == 2:
            if check[i-1] == 0:
                check[i] -= 1
                check[i-1] += 1
            elif check[i+1] == 0:
                check[i] -= 1
                check[i+1] += 1
                
    check = check[1:n+1]
    answer = n - check.count(0)
    return answer