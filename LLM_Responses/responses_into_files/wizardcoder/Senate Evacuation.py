def main():
    T = int(input())
    for i in range(1, T+1):
        N = int(input())
        parties = list(map(int, input().split()))
        plan = []
        while sum(parties) > 0:
            if max(parties) >= len(parties) // 2 + 1:
                max_party = max(enumerate(parties), key=lambda x: x[1])[0]
                plan.append(''.join([chr(max_party+65)]*min(2, parties[max_party]))
                parties[max_party] -= min(2, parties[max_party])
            else:
                for j in range(N):
                    if parties[j] > 0:
                        plan.append(''.join([chr(j+65)]*min(1, parties[j]))
                        parties[j] -= min(1, parties[j])
        print("Case #{}: {}".format(i, " ".join(plan))<|im_sep|>