def find_time(A, B, C):
    # Calculate total degrees of rotation for each hand
    A = (360 - A) % 360 * 12 / 360 * 1e9
    B = (360 - B) % 360 * 12 / 360 * 1e9
    C = (360 - C) % 360 * 12 / 360 * 1e9
    
    # Calculate time in nanoseconds
    total_time = A + B + C
    
    h, r = divmod(total_time, 3600*1e9)
    m, r = divmod(r, 60*1e9)
    s, n = divmod(r, 1e9)
    
    return int(h), int(m), int(s), int(n)

T = int(input())
for i in range(1, T+1):
    A, B, C = map(int, input().split())
    h, m, s, n = find_time(A, B, C)
    print("Case #{}: {} {} {} {}".format(i, h, m, s, n))