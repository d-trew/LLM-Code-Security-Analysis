T, B = map(int, input().split())

for _ in range(T):
    bits = ""
    for i in range(1, B + 1):
        print(i)
        bits += input()
    print(bits)