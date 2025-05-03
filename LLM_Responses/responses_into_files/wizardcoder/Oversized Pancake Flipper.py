import sys

def min_flips(pancakes, k):
    if len(pancakes) % (2 * k) != 0:
        return "IMPOSSIBLE"
    
    flipped = False
    count = 0
    for i in range(len(pancakes)):
        if pancakes[i] == "+":
            if not flipped and (i + k) < len(pancakes):
                pancakes[i:i+k] = ["-"] * k
                count += 1
                flipped = True
            elif flipped and i % k == 0:
                pancakes[i:i+k] = ["+"] * k
                count += 1
                flipped = False
    return count if all(pancake == "+" for pancake in pancakes) else "IMPOSSIBLE"
    
def main():
    T = int(input())
    for i in range(1, T + 1):
        S, K = input().split()
        K = int(K)
        print("Case #%d: %s" % (i, min_flips(S, K)) if len(S) >= K else "IMPOSSIBLE")
        
if __name__ == "__main__":
    main()