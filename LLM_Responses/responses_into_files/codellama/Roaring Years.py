T = int(input())
for _ in range(T):
    y = int(input())
    s = str(y)
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            k = int(s[i:j])
            if k > y and is_roaring(k):
                print(f"Case #{_+1}: {k}")
                break
def is_roaring(n):
    s = str(n)
    for i in range(1, len(s)):
        if s[:i] == str(i) and all(int(s[i+j]) == i+j for j in range(len(s)-i)):
            return True
    return False