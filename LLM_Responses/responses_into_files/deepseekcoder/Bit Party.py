def solve():
    T = int(input().strip())
    for t in range(T):
        R, B, C = map(int, input().split())
        max_bits = []
        scan_time = []
        pay_time = []
        for _ in range(C):
            m, s, p = map(int, input().split())
            max_bits.append(m)
            scan_time.append(s)
            pay_time.append(p)
        
        total_scan_time = sum([max_bits[i] * scan_time[i] for i in range(C)])
        min_pay_time = min(pay_time)

        result = max((total_scan_time + B*min_pay_time, R - 1))
        
        print('Case #{}: {}'.format(t+1, result))
solve()