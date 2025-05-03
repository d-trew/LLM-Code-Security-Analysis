import sys

def get_permutations(n):
    permutations = []
    for i in range(1, n+1):
        for p in range(i, n+1):
            if not any(j in [p1, p2] for j in range(1, p)):
                permutations.append([i, p])
    return permutations

def get_sorted_array(permutations, instructions, array):
    sorted_array = array.copy()
    for i in range(len(instructions)):
        permutation = permutations[instructions[i]-1]
        sorted_array = [sorted_array[j-1] if j in permutation else sorted_array[j] for j in range(1, len(array)+1)]
    return sorted_array

def main():
    T = int(input())
    for _ in range(T):
        P, S, K, N = map(int, input().split())
        permutations = get_permutations(N)
        for i in range(K):
            array = list(map(int, input().split()))
            instructions = list(map(int, input().split()))
            sorted_array = get_sorted_array(permutations, instructions, array)
            print(*sorted_array)

if __name__ == "__main__":
    main()