def main():
    T = int(input())
    for i in range(T):
        N, K = map(int, input().split())
        P = list(map(float, input().split()))
        
        # Calculate the probability of a tie
        max_prob = 0.0
        for j in range(N):
            for k in range(j+1, N):
                prob = min(P[j], P[k]) * (1 - max(P[j], P[k])) + max(P[j], P[k]) * (1 - min(P[j], P[k]))
                if K == 2:
                    max_prob = max(max_prob, prob)
        print("Case #{}: {}".format(i+1, max_prob))
        
if __name__ == "__main__":
    main()