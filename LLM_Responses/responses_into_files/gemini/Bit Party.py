def solve():
    R, B, C = map(int, input().split())
    cashiers = []
    for _ in range(C):
        cashiers.append(list(map(int, input().split())))

    min_time = float('inf')

    for i in range(1 << (R * C)):
        assignment = []
        bits_assigned = [0] * R
        cashier_used = [False] * C
        
        k=i
        valid_assignment = True
        for r in range(R):
            found_cashier = False
            for c in range(C):
                if (k % 2 == 1):
                    assignment.append((r,c))
                    found_cashier = True
                    break
                k //= 2
            if not found_cashier:
                valid_assignment = False
                break

        if not valid_assignment:
            continue

        
        
        
        robot_bits = [0] * R
        
        
        
        num_bits_remaining = B
        
        
        
        valid_bits_assignment = True
        for r,c in assignment:
            if num_bits_remaining ==0:
                valid_bits_assignment = False
                break
            
            
            
            robot_bits[r]+=1
            num_bits_remaining-=1
            
        if not valid_bits_assignment:
            continue
        
        
        
        
        
        
        cashier_usage = {}
        for r, c in assignment:
            if c not in cashier_usage:
                cashier_usage[c] = 0
            cashier_usage[c] += robot_bits[r]

        valid_assignment = True
        for c in cashier_usage:
          if cashier_usage[c] > cashiers[c][0]:
            valid_assignment = False
            break

        if not valid_assignment:
            continue

        max_time = 0
        for r, c in assignment:
            max_time = max(max_time, cashiers[c][1] * robot_bits[r] + cashiers[c][2])

        min_time = min(min_time, max_time)

    return min_time

T = int(input())
for i in range(1, T + 1):
    result = solve()
    print(f"Case #{i}: {result}")