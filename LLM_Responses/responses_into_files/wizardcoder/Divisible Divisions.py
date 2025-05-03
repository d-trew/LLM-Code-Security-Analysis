def count_divisible(s: str, d: int) -> int:
    def is_divisible(substring: str) -> bool:
        return int(substring) % d == 0
    
    n = len(s)
    result = 0
    for i in range(1 << (n-1):
        if not is_divisible(s[i]) and not is_divisible(s[i+1:i+2]):
            continue
        result += 1
    
    return result % (10**9 + 7)

def main():
    t = int(input())
    for i in range(t):
        s, d = input().split()
        print(f"Case #{i+1}: {count_divisible(s, int(d))}")
        
if __name__ == "__main__":
    main()