import re

def binary_to_int(s):
    return int(s, 2)

def int_to_binary(n):
    return bin(n)[2:].zfill(8)

def transform(s, e):
    s = int_to_binary(binary_to_int(s))
    e = int_to_binary(binary_to_int(e))

    # Initialize variables and counters
    steps = 0
    op1 = 0
    op2 = 0

    while s != e:
        if s[0] == '1':
            s = s[1:] + '0'
            op1 += 1
        elif s[-1] == '0':
            s = s[:-1] + '1'
            op2 += 1
        else:
            if len(s) > 1:
                s = s[1:] + s[0]
                op2 += 1
            else:
                break

        steps += max(op1, op2)
        op1, op2 = 0, 0

    return steps

def main():
    T = int(input())
    for _ in range(T):
        s, e = input().split()
        print(f"Case #{_+1}: {transform(s, e)}")

if __name__ == "__main__":
    main()