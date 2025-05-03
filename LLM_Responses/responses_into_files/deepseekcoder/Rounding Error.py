import math

def calculate_maximum_percentage():
    T = int(input())
    for t in range(1, T+1):
        N, L = map(int, input().split())
        C = list(map(int, input().split()))
        
        remaining = N - sum(C)
        max_val = 0

        if remaining > 0:
            total_percentage = (sum(C)-1)*2 + remaining*3
            while total_percentage % 10 != 0 and total_percentage % 5 != 4:
                total_percentage -= 1
            max_val += math.ceil((total_percentage / N) * 100)
        else:
            C = [c*2 for c in C]
        
        if remaining > 1 and sum(C[-2:]) < (N-remaining)*3:
            total_percentage += math.ceil(((N - sum(C[-2:])) / N) * 100)
            
        print("Case #{}: {}".format(t, max_val))

calculate_maximum_percentage()