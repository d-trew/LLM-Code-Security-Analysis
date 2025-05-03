import sys
sys.setrecursionlimit(10**6)
def dfs(graph, visited, news_values):
    global ans
    for i in range(len(visited)):
        if not visited[i] and (not news_values[i][0] or not news_values[i][1]) and abs(news_values[i][0]+news_values[i][1]) <= 32:
            visited[i] = True
            for j in graph[i]:
                if not visited[j-1]:
                    if news_values[i][0] and news_values[i][1]:
                        return False
                    
                    if not news_values[i][0]:
                        news_values[i][0] = 2**(len(graph)-1)
                        
                    if not news_values[i][1]:
                        news_values[j-1][1] = 2**(len(graph)-1)
                    
                    visited[j-1] = True
                    ans.append((i+1, j))
                    if dfs(graph, visited, news_values):
                        return True
                    else:
                        news_values[i][0], news_values[j-1][1] = 0, 0
                        ans.pop()
                        visited[j-1] = False
            visited[i] = False
            
def main():
    T = int(input())
    
    for i in range(T):
        F, P = map(int, input().split())
        
        graph = [[] for _ in range(F)]
        news_values = [[0, 0] for _ in range(F)]
        ans = []
        
        for j in range(P):
            A, B = map(int, input().split())
            graph[A-1].append(B)
            graph[B-1].append(A)
            
        visited = [False] * F
        
        if dfs(graph, visited, news_values):
            print("Case #{}: ".format(i+1), end="")
            for i in ans:
                print("{} {}".format(i[0], i[1]), end=" ")
            print()
        else:
            print("Case #{}: IMPOSSIBLE".format(i+1))
            
if __name__ == "__main__":
    main()