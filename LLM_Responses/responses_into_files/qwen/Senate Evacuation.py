def evacuate_senate(N, P):
    plan = []
    while sum(P) > 1:
        if len(plan) % 2 == 0:
            for i in range(26):
                if P[i] > 0:
                    plan.append(chr(i + ord('A')))
                    P[i] -= 1
                    break
        else:
            max_index = P.index(max(P))
            plan.append(chr(max_index + ord('A')))
            P[max_index] -= 1
    return ' '.join(plan)

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    T = int(data[0])
    index = 1
    results = []
    
    for _ in range(T):
        N = int(data[index])
        P = list(map(int, data[index + 1:index + N + 1]))
        index += N + 1
        result = evacuate_senate(N, P)
        results.append(f"Case #{_+1}: {result}")
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()