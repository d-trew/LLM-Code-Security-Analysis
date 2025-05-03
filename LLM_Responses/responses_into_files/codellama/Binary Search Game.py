import math

def binary_search(A, x):
    low = 0
    high = len(A) - 1
    while low <= high:
        mid = (low + high) // 2
        if A[mid] == x:
            return mid
        elif A[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def binary_search_game(A, cards):
    scores = []
    for card in cards:
        index = binary_search(A, card)
        if index != -1:
            scores.append(index + 1)
    return scores

def solve(N, M, L, A):
    scores = 0
    for i in range(M):
        cards = [random.randint(1, N) for _ in range(N)]
        scores += binary_search_game(A, cards)
    return scores % (10**9 + 7)

if __name__ == "__main__":
    T = int(input())
    for t in range(T):
        N, M, L = map(int, input().split())
        A = list(map(int, input().split()))
        print("Case #" + str(t+1) + ": " + solve(N, M, L, A))