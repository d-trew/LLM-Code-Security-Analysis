from math import factorial as fact
MOD = 10**9 + 7
facts = [1]
for i in range(1, 50*50+1):
    facts.append((facts[-1] * i) % MOD)
inv_facts = [pow(facts[-1], MOD-2, MOD)]
for i in range(50*50, 0, -1):
    inv_facts.append((inv_facts[-1] * i) % MOD)
inv_facts.reverse()
def binomial(n, k):
    return (facts[n] * ((inv_facts[k] * inv_facts[n-k]) % MOD)) % MOD
T = int(input())
for case in range(1, T+1):
    M, K = map(int, input().split())
    print('Case #{}: {}'.format(case, binomial((M*(M-1))//2, K-1)))