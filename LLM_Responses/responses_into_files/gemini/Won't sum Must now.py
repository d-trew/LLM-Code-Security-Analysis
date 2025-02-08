def is_palindrome(n):
    return str(n) == str(n)[::-1]

def solve():
    s = int(input())
    
    if is_palindrome(s):
        return str(s)

    for i in range(1, 100001):
        if is_palindrome(i):
            diff = s - i
            if is_palindrome(diff):
                return str(i) + " " + str(diff)
            
            for j in range(1, 100001):
                if is_palindrome(j):
                    diff2 = diff -j
                    if is_palindrome(diff2) and diff2 >=0:
                        return str(i) + " " + str(j) + " " + str(diff2)

    return "Not Found" #Should not reach here given the problem statement

t = int(input())
for i in range(1, t + 1):
    result = solve()
    print(f"Case #{i}: {result}")