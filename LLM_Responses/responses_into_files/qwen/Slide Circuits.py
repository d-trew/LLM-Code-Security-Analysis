from collections import defaultdict

def find_circuits(slides):
    n = len(slides)
    visited = [False] * n
    stack = []
    
    def dfs(node):
        if not visited[node]:
            visited[node] = True
            for neighbor in slides[node]:
                if not visited[neighbor]:
                    dfs(neighbor)
            stack.append(node)
    
    for i in range(n):
        dfs(i)
    
    def get_transpose():
        transpose = defaultdict(list)
        for u, v in slides.items():
            for w in v:
                transpose[w].append(u)
        return transpose
    
    def dfs_util(node, visited, component):
        if not visited[node]:
            visited[node] = True
            component.append(node)
            for neighbor in transpose[node]:
                dfs_util(neighbor, visited, component)
    
    transpose = get_transpose()
    components = []
    visited = [False] * n
    
    while stack:
        node = stack.pop()
        if not visited[node]:
            component = []
            dfs_util(node, visited, component)
            components.append(component)
    
    return components

def can_make_fun(slides, operations):
    n = len(slides)
    fun_states = [set() for _ in range(n)]
    
    for i in range(n):
        if not slides[i]:
            fun_states[i].add(i)
    
    for operation in operations:
        a, l, r, m = operation
        affected_slides = set(range(l - 1, r))
        multiple_of_m = {x for x in affected_slides if (x + 1) % m == 0}
        
        if a == 'E':
            for slide in multiple_of_m:
                fun_states[slide] -= {i for i in slides[slide]}
                fun_states[slide].add(slide)
        else:
            for slide in multiple_of_m:
                fun_states[slide] -= {slide}
                fun_states[slide] |= {i for i in slides[slide]}
    
    results = []
    for state in fun_states:
        if len(state) == 1:
            results.append(next(iter(state)) + 1)
        else:
            results.append('X')
    
    return ' '.join(map(str, results))

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    t = int(data[index])
    index += 1
    
    results = []
    
    for _ in range(t):
        b = int(data[index])
        s = int(data[index + 1])
        n = int(data[index + 2])
        index += 3
        
        slides = defaultdict(list)
        
        for _ in range(s):
            x = int(data[index]) - 1
            y = int(data[index + 1]) - 1
            slides[x].append(y)
            slides[y].append(x)
            index += 2
        
        operations = []
        
        for _ in range(n):
            a = data[index]
            l = int(data[index + 1])
            r = int(data[index + 2])
            m = int(data[index + 3])
            index += 4
            operations.append((a, l, r, m))
        
        result = can_make_fun(slides, operations)
        results.append(result)
    
    for i, result in enumerate(results):
        print(f"Case #{i+1}: {result}")

if __name__ == "__main__":
    solve()