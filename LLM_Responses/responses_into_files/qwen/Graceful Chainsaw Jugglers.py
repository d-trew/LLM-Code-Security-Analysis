def max_jugglers(R, B):
    return min(R + 1, B + 1)

T = int(input())
results = []
for i in range(1, T + 1):
    R, B = map(int, input().split())
    results.append(f"Case #{i}: {max_jugglers(R, B)}")

for result in results:
    print(result)