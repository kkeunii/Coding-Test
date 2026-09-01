def solution(tickets):
    
    routes = {}
    for t in tickets:
        routes[t[0]] = routes.get(t[0], []) + [t[1]]
    
    for r in routes:
        routes[r].sort(reverse = True)
        
    stack = ['ICN']
    answer = []
    while stack:
        now = stack[-1]
        if now not in routes or len(routes[now]) == 0:
            answer.append(stack.pop())
        else:
            stack.append(routes[now][-1])
            routes[now].pop()
    return answer[::-1]
        
        
    
    