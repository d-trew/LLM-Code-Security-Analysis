def min_operations_to_sort(N, X):
    operations = 0
    for i in range(1, N):
        if X[i] <= X[i - 1]:
            diff = X[i - 1] - X[i] + 1
            operations += diff
            X[i] = X[i - 1] + 1
    return operations

def solve():
    T = int(input())
    for t in range(1, T + 1):
        N = int(input())
        X = list(map(int, input().split()))
        result = min_operations_to_sort(N, X)
        print(f"Case #{t}: {result}")

if __name__ == "__main__":
    solve()