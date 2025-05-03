def find_max_fences(poles, existing_fences):
    n = len(poles)
    edges = []
    
    # Add all possible fences between non-collinear poles
    for i in range(n):
        for j in range(i + 1, n):
            if (poles[j][1] - poles[i][1]) * (poles[j][0] - existing_fences[0][0]) != \
               (poles[j][1] - existing_fences[0][1]) * (poles[j][0] - poles[i][0]):
                edges.append((i, j))
    
    # Remove fences that intersect with existing fences
    valid_edges = []
    for edge in edges:
        i, j = edge
        if not any((poles[i][1] - poles[j][1]) * (existing_fences[k][1] - poles[i][1]) == \
                   (existing_fences[k][1] - poles[j][1]) * (existing_fences[k][0] - poles[i][0]) and
                   (poles[j][0] - poles[i][0]) * (existing_fences[k][0] - poles[i][0]) > 0 for k in range(2)):
            valid_edges.append(edge)
    
    # Find the maximum number of non-intersecting fences
    max_fences = []
    visited = set()
    for i, j in valid_edges:
        if i not in visited and j not in visited:
            max_fences.append((i, j))
            visited.add(i)
            visited.add(j)
    
    return len(max_fences), max_fences

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    T = int(data[index])
    index += 1
    
    results = []
    
    for t in range(1, T + 1):
        N = int(data[index])
        index += 1
        
        poles = []
        for _ in range(N):
            x = int(data[index])
            y = int(data[index + 1])
            index += 2
            poles.append((x, y))
        
        existing_fences = [(int(data[index]), int(data[index + 1])), (int(data[index + 2]), int(data[index + 3]))]
        index += 4
        
        max_fences_count, max_fences = find_max_fences(poles, existing_fences)
        
        results.append(f"Case #{t}: {max_fences_count}")
        for i, j in max_fences:
            results.append(f"{i} {j}")
    
    print("\n".join(results))

if __name__ == "__main__":
    main()