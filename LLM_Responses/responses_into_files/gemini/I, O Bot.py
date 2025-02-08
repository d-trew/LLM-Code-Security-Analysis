def solve():
    N, C = map(int, input().split())
    balls = []
    for _ in range(N):
        balls.append(list(map(int, input().split())))

    zeros = []
    ones = []
    for ball in balls:
        if ball[1] == 0:
            zeros.append(abs(ball[0]))
        else:
            ones.append(abs(ball[0]))

    zeros.sort()
    ones.sort()

    total_power = 0
    
    zero_compartment = False
    one_compartment = False

    
    i = 0
    j = 0
    while i < len(zeros) or j < len(ones):
        
        if i < len(zeros) and (j == len(ones) or zeros[i] <= ones[j]):
            total_power += 2 * zeros[i]
            i += 1
            
        elif j < len(ones):
            total_power += 2 * ones[j]
            j+=1

    return total_power


T = int(input())
for i in range(1, T + 1):
    result = solve()
    print(f"Case #{i}: {result}")