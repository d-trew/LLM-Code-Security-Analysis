def solve():
    P, S, K, N = map(int, input().split())
    arrays = []
    for _ in range(K):
        arrays.append(list(map(int, input().split())))

    # Define permutations (example: using only two permutations for simplicity)
    permutations = [
        list(range(1, N + 1)),  # Identity permutation
        list(range(N, 0, -1))   # Reverse permutation
    ]
    
    print(len(permutations))
    for p in permutations:
        print(*p)

    for arr in arrays:
        instructions = []
        sorted_arr = sorted(arr)
        
        #Simple strategy: alternate between identity and reverse until sorted.  This will not always be optimal within the S limit.
        
        current_arr = arr[:]
        while current_arr != sorted_arr:
            if current_arr == arr:
                instructions.append(1) #identity
                current_arr = current_arr[:]
            elif current_arr == sorted_arr:
                break
            else:
                instructions.append(2) #reverse
                current_arr = current_arr[::-1]
            

        print(len(instructions), *instructions)



T = int(input())
for i in range(1, T + 1):
    print(f"Case #{i}:")
    solve()