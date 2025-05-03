import re
for _ in range(int(input())):
    a, b = map(int, input().split())
    pattern = re.compile(input())
    count = sum(1 for i in range(a, b+1) if bool(pattern.match(str(i))))
    print(f"Case # {_+1}: {count}")