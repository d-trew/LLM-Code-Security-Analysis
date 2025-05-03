from fractions import Fraction
import sys
input = sys.stdin.readline

def gcd(a, b):
    while b: a, b = b, a % b
    return a

T = int(input())
for t in range(1, T+1):
    N, K = map(int, input().split())
    U = Fraction(*map(Fraction, input().split()))
    P = list(map(Fraction, input().split()))

    # Calculate the maximum probability of success if all cores are trained to 1
    max_prob = (1 - U / N) ** (N - K)

    # Calculate the minimum probability of success for each core individually
    min_prob = [(P[i] * (1 - U / N)) ** (N - K) for i in range(N)]

    # Find the maximum probability among all possible assignments
    max_assignment = max([min(sum(min_prob), 1.0) for min_prob in itertools.combinations(min_prob, N-K)])

    print('Case #{}: {}'.format(t, max_assignment))