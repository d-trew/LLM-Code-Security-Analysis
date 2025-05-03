def main():
    T = int(input())
    for i in range(T):
        N, K = map(int, input().split())
        P_set = set(map(int, input().split()))
        max_win_prob = 0.0
        for a in range(1, K+1):
            for b in range(a+1, K+1):
                if len(P_set) == N:
                    win_prob = (N/K)**2
                else:
                    P_set.add(a)
                    P_set.add(b)
                    win_prob = ((len(P_set)-1)/K)**2 + 2*(a==b)*((N+1)/K)**2 - (2*a==b)*((N-1)/K)**2
                max_win_prob = max(max_win_prob, win_prob)
        print("Case #%d: %.6f" % (i+1, max_win_prob))