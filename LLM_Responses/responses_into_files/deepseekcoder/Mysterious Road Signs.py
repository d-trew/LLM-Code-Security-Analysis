def solve():
    T = int(input())
    for case in range(1, T+1):
        S = int(input())
        signs = []
        for _ in range(S):
            Di, Ai, Bi = map(int, input().split())
            signs.append((Di, Ai, Bi))
        
        valid_sets = 0
        max_length = 0
        curr_length = 1
        prev_A = signs[0][1]
        for i in range(1, S):
            if signs[i][2] == prev_A:
                curr_length += 1
                if signs[i][0] - signs[i-1][0] == 1 and curr_length > max_length:
                    max_length = curr_length
            else:
                curr_length = 1
            prev_A = signs[i][1]
        
        if max_length > 2:
            valid_sets = (max_length-1) * max_length // 2
        print(f"Case #{case}: {max_length} {valid_sets}")

solve()