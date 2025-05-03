def solve(case_num, N, L, R):
    result = 'IMPOSSIBLE'
    if N <= 100:
        graph = [[] for _ in range(N+1)]
        visited = [False]*(N+1)
        mascots = ['A', 'C', 'D', 'E', 'H', 'I', 'J', 'K', 'M', 'O', 'R', 'S', 'T']
        for i in range(1, N+1):
            graph[L[i-1]].append((i, R[i-1]))
            graph[R[i-1]].append((i, L[i-1]))
        
        def dfs(node, prev_mascot):
            nonlocal result
            if visited[node]:
                return []
            visited[node] = True
            
            for next_node, _ in graph[node]:
                if not visited[next_node]:
                    temp = dfs(next_node, prev_mascot)
                    if temp == 'IMPOSSIBLE':
                        return 'IMPOSSIBLE'
                    elif len(temp) == 3 and temp[0] != temp[-1]:
                        return 'IMPOSSIBLE'
                    else:
                        return [prev_mascot] + temp + [prev_mascot]
            
            if not result == 'IMPOSSIBLE':
                for i in range(len(result)//2):
                    if result[i] == result[-1-i]:
                        break
                else:
                    return [prev_mascot]
                    
            return 'IMPOSSIBLE'
        
        for mascot in mascots:
            visited = [False]*(N+1)
            temp = dfs(1, mascot)
            if not temp == 'IMPOSSIBLE':
                result = temp[len(temp)//2:] + temp[:len(temp)//2][::-1]
                break
    
    print('Case #{}: {}'.format(case_num, result))