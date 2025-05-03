def max_outfits(J, P, S, K):
    if J == 1 and P == 1:
        return 1, [(1, 1, i) for i in range(1, S + 1)]
    elif J == 2 and P == 2:
        return 4, [(1, 1, i), (1, 2, i), (2, 1, i), (2, 2, i) for i in range(1, min(S, K + 1))]
    else:
        return J * P * S // max(J * P, P * S, J * S), [(j, p, s) for j in range(1, J + 1) for p in range(1, P + 1) for s in range(1, S + 1)]

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    T = int(data[0])
    index = 1
    results = []
    
    for _ in range(T):
        J = int(data[index])
        P = int(data[index + 1])
        S = int(data[index + 2])
        K = int(data[index + 3])
        index += 4
        
        max_days, outfits = max_outfits(J, P, S, K)
        results.append((max_days, outfits))
    
    for i, (days, outfits) in enumerate(results):
        print(f"Case #{i+1}: {days}")
        for outfit in outfits:
            print(" ".join(map(str, outfit)))

if __name__ == "__main__":
    solve()