def calculate_reversort_cost(N, L):
    total_cost = 0
    for i in range(1, N):
        min_index = L.index(min(L[i:])) + i
        total_cost += (min_index - i) + 1
        L = L[:i] + L[min_index:i-1:-1] + L[min_index+1:]
    return total_cost

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    T = int(data[0])
    index = 1
    results = []
    
    for _ in range(T):
        N = int(data[index])
        L = list(map(int, data[index + 1:index + N + 1]))
        index += N + 1
        cost = calculate_reversort_cost(N, L)
        results.append(f"Case #{_ + 1}: {cost}")
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()