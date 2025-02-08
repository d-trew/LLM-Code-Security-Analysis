import random
import math

def sigmoid(x):
    return 1 / (1 + math.exp(-x))

def solve():
    results = []
    for _ in range(100):
        results.append(input())

    success_rates = []
    for i in range(100):
        success_count = 0
        for j in range(10000):
            if results[i][j] == '1':
                success_count += 1
        success_rates.append(success_count / 10000)

    #Heuristic: The cheater will likely have the highest success rate.
    cheater = success_rates.index(max(success_rates)) + 1
    return cheater

T = 50
P = 86

for i in range(1, T + 1):
    result = solve()
    print(f"Case #{i}: {result}")