def main():
    T = int(input())
    for i in range(T):
        A, B = map(int, input().split())
        R = random.randint(A, B)
        X, Y = random.sample([-109, 109], 2)
        for j in range(300):
            x, y = map(int, input().split())
            if (x - X) ** 2 + (y - Y) ** 2 <= R ** 2:
                print("CENTER")
                break
            else:
                print("WRONG")
        else:
            continue
    print("CORRECT")

if __name__ == "__main__":
    main()