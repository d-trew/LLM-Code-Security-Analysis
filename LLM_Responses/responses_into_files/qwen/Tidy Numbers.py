def is_tidy(n):
    digits = str(n)
    return all(digits[i] <= digits[i + 1] for i in range(len(digits) - 1))

def find_last_tidy(N):
    while not is_tidy(N):
        N -= 1
    return N

T = int(input())
results = []
for t in range(1, T + 1):
    N = int(input())
    last_tidy = find_last_tidy(N)
    results.append(f"Case #{t}: {last_tidy}")

for result in results:
    print(result)