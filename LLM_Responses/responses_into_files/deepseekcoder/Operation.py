from fractions import Fraction
import sys

def solve():
    C = int(input().split()[1])
    cards = [tuple(map(str, input().split())) for _ in range(C)]
    
    dp = [[Fraction(0) for _ in range(2*len(cards)+1)] for _ in range(len(cards)+1)]
    dp[0][0] = Fraction(input())
    
    for i in range(C):
        op, v = cards[i]
        v = int(v)
        
        for j in reversed(range(2*len(cards))):
            for k in reversed(range(j+1)):
                if dp[i][k]:
                    if op == '+':
                        dp[i+1][j] = max(dp[i+1][j], dp[i][k] + v)
                    elif op == '-':
                        dp[i+1][j] = max(dp[i+1][j], dp[i][k] - v)
                    elif op == '*':
                        dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][k] * v)
                    else: # '/'
                        if v != 0:
                            dp[i+1][j+2] = max(dp[i+1][j+2], dp[i][k] / v)
    
    return str(max((x for x in dp[-1] if x.denominator == 1 and x != 0), key=lambda f: abs(f)))

T = int(input())
for t in range(1, T+1):
    print('Case #{}: {}'.format(t, solve()))