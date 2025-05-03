def flip_pancakes(K, S):
    count = 0
    for i in range(len(S) - K + 1):
        if (sum([S[j] == '+' for j in range(i, min(i+K, len(S))]) != K):
            return "IMPOSSIBLE"
        S[i:i+K] = ['-'] * K
        count += 1
    return count

T = int(input())
for _ in range(T):
    S, K = input().split()
    print("Case #{}: {}".format(_ + 1, flip_pancakes(int(K), list(S)))