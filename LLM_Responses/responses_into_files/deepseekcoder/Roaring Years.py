def next_roaring(y):
    y += 1
    while True:
        str_y = str(y)
        is_roaring = all([str(i+1) in str_y for i in range(len(str_y)-1)])
        if is_roaring and len(set(str_y)) == len(str_y):
            return y
        y += 1

def main():
    T = int(input())
    for case in range(1, T+1):
        Y = int(input())
        print('Case #{}: {}'.format(case, next_roaring(Y)))

if __name__ == "__main__":
    main()