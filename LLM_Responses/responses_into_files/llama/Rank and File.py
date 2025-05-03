t = int(input())
for _ in range(t):
    n = int(input())
    row = set()
    col = set()
    for i in range(2*n-1):
        if i < n:
            row.update(map(int, input().split()))
        else:
            col.update(map(int, input().split()))
    if len(row) == n:
        missing = sorted(set(range(min(row), max(row)+1)))
    else:
        missing = sorted(set(range(min(col), max(col)+1)))
    print(f"Case # {_+1}: {missing}")