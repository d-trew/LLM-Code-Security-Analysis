def generate_spanning_trees(K):
    if K == 3:
        return 3, [[0, 1, 1], [1, 0, 0], [1, 0, 0]]
    elif K == 4:
        return 4, [[0, 1, 1, 1], [1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0]]
    else:
        return K, [[0] * K for _ in range(K)]

def main():
    T = int(input())
    results = []
    
    for i in range(T):
        K = int(input())
        num_nodes, graph = generate_spanning_trees(K)
        results.append((i + 1, num_nodes, graph))
    
    for case_num, num_nodes, graph in results:
        print(f"Case #{case_num}: {num_nodes}")
        for row in graph:
            print(''.join(map(str, row)))

if __name__ == "__main__":
    main()