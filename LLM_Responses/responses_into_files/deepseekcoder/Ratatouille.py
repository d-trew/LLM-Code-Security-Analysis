T = int(input())
for _ in range(T):
    N, P = map(int, input().split())
    packages = []
    for _ in range(N):
        package = list(map(int, input().split()))
        packages.append(package)
    max_kits = 0
    for i in range(1 << N):
        valid = True
        kit_serving = 0
        total_packages = [0] * P
        for j in range(N):
            if (i & (1 << j)):
                kit_serving += 1
                for k in range(P):
                    total_packages[k] += packages[j][k]
        for j in range(P):
            if packages[0][j] * .9 <= total_packages[j] <= packages[0][j] * 1.1:
                continue
            valid = False
            break
        if valid and kit_serving > max_kits:
            max_kits = kit_serving
    print(f"Case # {_ + 1}: {max_kits}")