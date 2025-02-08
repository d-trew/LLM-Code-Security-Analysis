def solve():
    S = input()
    count = 0
    for i in range(len(S) - 1):
        if S[i] != S[i+1]:
            count += 1
    if S[-1] == '-':
        count += 1
    return count

T = int(input())
for i in range(1, T + 1):
    result = solve()
    print(f"Case #{i}: {result}")