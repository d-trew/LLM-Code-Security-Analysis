import math

def find_shortcut(n):
    shortcut = []
    x, y = 1, n * n - 1
    while x != y:
        if x + 1 == y or y + 1 == x:
            break
        if (x % n) // (n - 1) == 0 and (y % n) // (n - 1) == 0:
            shortcut.append((x, y))
            return shortcut
        elif (x % n) < (y % n):
            x += math.ceil(n / 2) if n > 3 else 2
            y -= math.ceil(n / 2) if n > 3 else 1
        else:
            x += math.floor(n / 2) if n > 3 else 2
            y -= math.floor(n / 2) if n > 3 else 1
    return shortcut

def main():
    t = int(input())
    
    for i in range(t):
        n, k = map(int, input().split())
        
        if k >= n * n - 1:
            print("Case #{}: IMPOSSIBLE".format(i + 1))
        else:
            shortcuts = find_shortcut(n)
            
            if len(shortcuts) < k:
                print("Case #{}: {}".format(i + 1, len(shortcuts))
                for s in shortcuts[:k]:
                    print(*s)
            else:
                print("Case #{}: IMPOSSIBLE".format(i + 1))

if __name__ == "__main__":
    main()