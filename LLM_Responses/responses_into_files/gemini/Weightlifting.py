def solve():
    E, W = map(int, input().split())
    exercises = []
    for _ in range(E):
        exercises.append(list(map(int, input().split())))

    min_ops = float('inf')

    def count_operations(path):
        ops = 0
        stack = []
        for i in range(E):
            needed = exercises[i]
            
            to_add = []
            to_remove = []

            for j in range(W):
                diff = needed[j] - stack.count(j+1)
                if diff > 0:
                    to_add.extend([j+1] * diff)
                elif diff < 0:
                    to_remove.extend([j+1] * abs(diff))

            
            ops += len(to_add)
            stack.extend(to_add)
            
            
            
            ops += len(to_remove)
            
            for k in range(len(to_remove)):
              if stack[-1] != to_remove[-k-1]:
                print("Error: stack mismatch")
                return float('inf')
              stack.pop()

        return ops

    
    import itertools
    
    all_perms = []
    for i in range(E):
        num_weights = sum(exercises[i])
        all_perms.append(list(itertools.permutations(range(1,W+1), num_weights)))
    
    
    for perm_tuple in itertools.product(*all_perms):
      
      
      combined_perm = []
      for perm in perm_tuple:
          combined_perm.extend(list(perm))
      
      
      
      
      ops = count_operations(combined_perm)
      min_ops = min(min_ops,ops)


    return min_ops

T = int(input())
for i in range(1, T + 1):
    result = solve()
    print(f"Case #{i}: {result}")