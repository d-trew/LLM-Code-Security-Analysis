def solve():
    N, D = map(int, input().split())
    A = list(map(int, input().split()))

    min_cuts = float('inf')

    for i in range(1 << N):
        total_angle = 0
        num_slices = 0
        angles = []
        for j in range(N):
            if (i >> j) & 1:
                total_angle += A[j]
                num_slices += 1
                angles.append(A[j])

        if num_slices > 0:
            target_angle = total_angle / D
            cuts_needed = 0
            
            if all(abs(angle - target_angle) < 1e-9 for angle in angles):
                min_cuts = min(min_cuts, cuts_needed)
                continue
            

            
            for k in range(num_slices):
              
              num_cuts_for_slice = 0
              current_angle = angles[k]
              
              if abs(current_angle - target_angle) > 1e-9:
                num_cuts_for_slice = 0
                while current_angle > target_angle:
                    current_angle -= target_angle
                    num_cuts_for_slice +=1
                cuts_needed += num_cuts_for_slice

            min_cuts = min(min_cuts, cuts_needed)
    

    
    if min_cuts == float('inf'):
        min_cuts = D -1

    return min_cuts

T = int(input())
for i in range(1, T + 1):
    result = solve()
    print(f"Case #{i}: {result}")