import sys

def get_pair(n):
    if n == 4:
        return (1, 3)
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            b = n // i
            if len(str(i)) < len(str(b)):
                return (i, b)
    return (n, 1)

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        a, b = get_pair(n)
        print('Case #x:', a, b)