import math

def solve(n, s, b):
    count = 0
    for i in range(1 << n):  # iterate over all possible configurations
        has_cat_last_box = False
        has_cat_in_last_box = False
        cat_in_last_box = (s[-1] == 'C')
        
        for j in range(n-1):
            if s[j] == '?':
                s_j = 'C' if ((i >> j) & 1) else '.'
            else:
                s_j = s[j]
            
            if s_j == 'C':
                has_cat_last_box = True
                for k in range(j+1, n):
                    if s[k] == '?':
                        s_k = 'C' if ((i >> k) & 1) else '.'
                    else:
                        s_k = s[k]
                    
                    if s_k == '.' and b[j] != k:
                        has_cat_last_box = False
                        break
                    
                if has_cat_last_box:
                    for k in range(j+1, n):
                        if s[k] == '?':
                            s_k = 'C' if ((i >> k) & 1) else '.'
                        else:
                            s_k = s[k]
                        
                        if s_k == 'C' and b[j] != k:
                            has_cat_in_last_box = True
                            break
                    
        if cat_in_last_box and not has_cat_in_last_box:
            count += 1
            
    return count % (10**9 + 7)

t = int(input())
for i in range(t):
    n = int(input())
    s = input()
    b = list(map(int, input().split()))
    print(f"Case #{i+1}: {solve(n, s, b)}")