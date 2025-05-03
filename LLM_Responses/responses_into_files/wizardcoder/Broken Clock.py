import math
def calculate_time(A, B, C):
    h = (B - A) / 3600 * 12 % 12
    m = (C - B) / 60 % 60
    s = (C - A) / 720 % 60
    n = ((C - A) % 720) * 1e9 // 720 % 1e9
    return f"Case #{case+1}: {int(h)} {int(m)} {int(s)} {int(n)}"
    
T = int(input())
for case in range(T):
    A, B, C = map(float, input().split())
    print(calculate_time(A, B, C))