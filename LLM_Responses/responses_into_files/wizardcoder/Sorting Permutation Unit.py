import math

def sort_array(arr):
    return sorted(arr)

def main():
    T = int(input())
    for i in range(T):
        P, S, N, K = map(int, input().split())
        arrays = [list(map(int, input().split())) for _ in range(K)]
        permutations = []
        for j in range(P):
            permutation = list(map(int, input().split()))
            permutations.append([permutation[i] - 1 for i in range(N)])
        
        instructions = []
        for k in range(K):
            S_prime = int(input())
            if S_prime > S:
                print("Invalid input")
                return
            instruction = [int(x) - 1 for x in input().split()]
            if len(set(instruction)) != len(instruction):
                print("Invalid input")
                return
            instructions.append(instruction)
        
        for k in range(K):
            sorted_array = arrays[k][:]
            for s in instructions[k]:
                sorted_array = sort_array([sorted_array[permutations[s][i] - 1] for i in range(N)] if len(instructions[k]) == S else sort_array(sorted_array)
            print(" ".join(map(str, sorted_array))
            
if __name__ == "__main__":
    main()