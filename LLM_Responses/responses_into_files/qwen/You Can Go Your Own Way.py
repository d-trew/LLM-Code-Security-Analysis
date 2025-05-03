def find_path(N, path):
    moves = {'E': 'S', 'S': 'E'}
    new_path = []
    i = 0
    while i < len(path):
        if path[i] == 'E':
            if i + 1 < len(path) and path[i+1] == 'S':
                new_path.append(moves[path[i]])
                i += 2
            else:
                new_path.append(path[i])
                i += 1
        elif path[i] == 'S':
            if i + 1 < len(path) and path[i+1] == 'E':
                new_path.append(moves[path[i]])
                i += 2
            else:
                new_path.append(path[i])
                i += 1
    return ''.join(new_path)

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    T = int(data[0])
    results = []
    index = 1
    
    for _ in range(T):
        N = int(data[index])
        path = data[index + 1]
        index += 2
        
        result = find_path(N, path)
        results.append(f"Case #{_+1}: {result}")
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()