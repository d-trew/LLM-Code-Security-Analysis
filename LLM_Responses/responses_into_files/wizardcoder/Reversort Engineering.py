import sys
from collections import defaultdict

def reversort(n, c):
    if n == 1 and c != 0:
        return "IMPOSSIBLE"
    elif c < n - 1 or c > (n * (n-1) // 2):
        return "IMPOSSIBLE"
    
    result = []
    for i in range(1, n+1):
        if not result:
            result.append(i)
        
        elif len(result) == c - (n-i):
            result.insert(0, i)
        
        else:
            result.append(i)
    
    return " ".join([str(x) for x in result] if len(set(result)) == n else "IMPOSSIBLE"

def main():
    t = int(input())
    for i in range(1, t+1):
        n, c = map(int, input().split())
        print("Case #{}: {}".format(i, reversort(n, c)) if len(reversort(n, c)) != 1 else "IMPOSSIBLE")

if __name__ == '__main__':
    main()