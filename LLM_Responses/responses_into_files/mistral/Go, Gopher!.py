T = int(input())
for _ in range(T):
    A = int(input())
    prepared = set()
    for _ in range(1000):
        while True:
            I, J = map(int, input().split())
            if (I, J) not in prepared and 2 <= I <= 999 and 2 <= J <= 999:
                break
        prepared.add((I, J))
        print(I, J)
        response = input().split()
        if response == ['0', '0']:
            break