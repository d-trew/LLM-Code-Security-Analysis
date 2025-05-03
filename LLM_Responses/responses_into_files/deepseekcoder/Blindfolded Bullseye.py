T, A, B = map(int, input().split())
for _ in range(T):
    for _ in range(300):
        r = (A + B) // 2
        x = int(input())
        y = int(input())
        if ((x**2 + y**2)**0.5 - r) % 1 < 10**(-9):
            print("CENTER")
            break
        elif (abs(x) > 109 or abs(y) > 109):
            print("WRONG")
            exit()
    else:
        print("CENTER")