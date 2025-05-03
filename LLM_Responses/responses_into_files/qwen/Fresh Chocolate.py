def maximize_fresh_chocolate(N, P, groups):
    fresh_chocolate = 0
    leftover = 0
    
    for group in groups:
        if group > P + leftover:
            continue
        elif group == P + leftover:
            fresh_chocolate += 1
            leftover = 0
        else:
            fresh_chocolate += 1
            leftover = (P + leftover) % group
    
    return fresh_chocolate

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    T = int(data[0])
    index = 1
    results = []
    
    for _ in range(T):
        N = int(data[index])
        P = int(data[index + 1])
        groups = list(map(int, data[index + 2:index + 2 + N]))
        index += 2 + N
        
        result = maximize_fresh_chocolate(N, P, groups)
        results.append(f"Case #{_+1}: {result}")
    
    for result in results:
        print(result)

if __name__ == "__main__":
    solve()