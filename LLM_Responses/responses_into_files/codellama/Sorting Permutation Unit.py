import sys

def solve(input):
    # Read input
    T = int(input())
    for t in range(T):
        P, S, K, N = map(int, input().split())
        arrays = []
        for _ in range(K):
            array = list(map(int, input().split()))
            arrays.append(array)
    
    # Sort each array using the same permutation instruction
    for array in arrays:
        sorted_array = sorted(array)
        print(*sorted_array)

if __name__ == "__main__":
    input = sys.stdin.read()
    solve(input)