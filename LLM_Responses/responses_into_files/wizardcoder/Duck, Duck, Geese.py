import sys
from itertools import combinations

def count_valid_choices(N, C, A, B, P):
    def is_valid(choice):
        counts = [0] * C
        for i in range(len(choice)):
            player = choice[i] - 1
            color = P[player]
            if choice[i+1] == N: # wrap around to beginning of list
                player = 0
            counts[color-1] += 1
        return all([A[c] <= counts[c] <= B[c] for c in range(C)])

    valid_choices = [list(combinations(range(N), i)) for i in range(2, N)]
    valid_choices = sum([filter(is_valid, choices) for choices in valid_choices], [])
    return len(valid_choices)

def main():
    T = int(input())
    for case in range(1, T+1):
        N, C = map(int, input().split())
        A = []
        B = []
        P = [0] * N # initialize with 0 to avoid index out of range errors
        for i in range(C):
            a, b = map(int, input().split())
            A.append(a)
            B.append(b)
        P = list(map(int, input().split()))
        print("Case #{}: {}".format(case, count_valid_choices(N, C, A, B, P))

if __name__ == "__main__":
    main()