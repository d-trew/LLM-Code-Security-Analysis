import sys

def fashion_police(j, p, s, k):
    jackets = []
    pants = []
    shirts = []
    
    for i in range(1, j + 1):
        for j in range(1, p + 1):
            for k in range(1, s + 1):
                if (i, j, k) not in jackets:
                    jackets.append((i, j, k))
    return jackets

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        j, p, s, k = map(int, input().split())
        outfits = fashion_police(j, p, s, k)
        print("Case #%d: %d" % (i + 1, len(outfits)))
        for o in outfits:
            print(*o)