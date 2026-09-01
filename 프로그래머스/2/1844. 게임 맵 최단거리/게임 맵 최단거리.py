def solution(maps):
    
    queue = []
    directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    row = len(maps)
    col = len(maps[0])
    path = [[0] * col for _ in range(row)]
    visited = [[False] * col for _ in range(row)]
    
    path[0][0] = 1
    visited[0][0] = True
    queue.append((0,0))
    
    while queue:
        x, y = queue.pop(0)
        for a, b in directions:
            nx = x + a
            ny = y + b
            if 0 <= nx < row and 0 <= ny < col and visited[nx][ny] == False and maps[nx][ny] == 1:
                queue.append((nx, ny))
                visited[nx][ny] = True
                path[nx][ny] = path[x][y] + 1
                
    if path[row-1][col-1] == 0:
        return -1
    else:
        return path[row-1][col-1]