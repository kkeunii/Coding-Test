def solution(board):
    '''
    n = len(board)
    
    answer = [[0 for col in range(n+2)] for row in range(n+2)]
    direction = [(0, 1), (1, 0), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1),(-1, -1)]
    
    for row in range(0, n):
        for col in range(0, n):
            if board[row][col] == 1:
                answer[row+1][col+1] = 1
                for dx, dy in direction:
                    nx, ny = row+1 + dx, col+1 + dy
                    answer[nx][ny] = 1
    total_count = 0
    for i in answer[1:n+1]:
        for j in i[1:n+1]:
            if j == 0:
                total_count +=1 
    '''
    count = 0
    n = len(board)
    direction = [(x, y) for x in (-1, 0, 1) for y in (-1, 0, 1)]
    for row in range(0, n):
        for col in range(0, n):
            for dx, dy in direction:
                if (0 <= row+dx < n and 0 <= col+dy < n) and board[row+dx][col+dy] == 1:
                    count += 1
                    break
            
                
    return n*n - count 