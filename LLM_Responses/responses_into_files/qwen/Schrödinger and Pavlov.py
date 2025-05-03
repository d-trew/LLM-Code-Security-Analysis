MOD = 10**9 + 7

def count_configurations(N, S, B):
    if '?' not in S:
        return int(S[-1] == 'C')
    
    unknown_indices = [i for i in range(N) if S[i] == '?']
    num_unknowns = len(unknown_indices)
    
    if N - 1 in unknown_indices:
        return (2 ** (num_unknowns - 1)) % MOD
    
    last_box_index = unknown_indices[-1]
    first_box_with_tunnel_to_last = None
    for i in range(last_box_index):
        if B[i] == last_box_index + 1:
            first_box_with_tunnel_to_last = i
            break
    
    if first_box_with_tunnel_to_last is None:
        return (2 ** num_unknowns) % MOD
    
    configurations = 0
    for i in range(2 ** num_unknowns):
        config = [False] * N
        for j in range(num_unknowns):
            if i & (1 << j):
                config[unknown_indices[j]] = True
        
        current_box = first_box_with_tunnel_to_last
        while current_box != last_box_index:
            next_box = B[current_box]
            if not config[next_box - 1]:
                break
            current_box = next_box - 1
        
        if current_box == last_box_index and not any(config):
            configurations += 1
    
    return configurations % MOD

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    T = int(data[0])
    index = 1
    results = []
    
    for _ in range(T):
        N = int(data[index])
        S = data[index + 1]
        B = list(map(int, data[index + 2:index + 2 + N]))
        
        result = count_configurations(N, S, B)
        results.append(result)
        
        index += 2 + N
    
    for i, result in enumerate(results):
        print(f"Case #{i+1}: {result}")

if __name__ == "__main__":
    main()