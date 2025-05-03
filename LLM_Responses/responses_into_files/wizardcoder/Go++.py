import sys

def check_output(bad, good):
    if len(good) == 0 or len(bad) != len(good[0]):
        return "IMPOSSIBLE"
    
    for g in good:
        if set(g) - set(bad):
            return "IMPOSSIBLE"
        
    program1 = ""
    program2 = ""
    count = 0
    
    for i, c in enumerate(bad):
        if bad[i] == '0' and len(good) * '0' not in good:
            program1 += "?"
            program2 += "0"
        elif bad[i] == '1' and len(good) * '1' not in good:
            program1 += "1"
            program2 += "?"
        else:
            return "IMPOSSIBLE"
        
    if count > 200:
        return "IMPOSSIBLE"
    
    return f"{program1}\n{program2}"

def main():
    T = int(input())
    for i in range(1, T + 1):
        N, L = map(int, input().split())
        good = [input() for _ in range(N)]
        bad = input()
        
        result = check_output(bad, good)
        print(f"Case #{i}: {result}")

if __name__ == "__main__":
    main()