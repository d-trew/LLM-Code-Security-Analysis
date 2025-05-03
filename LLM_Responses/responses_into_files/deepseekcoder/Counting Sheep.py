def count_sheep(N):
    if N == 0:
        return "INSOMNIA"
    
    digits = set()
    i = 1
    while len(digits) < 10:
        number = i * N
        digits.update(str(number))
        i += 1
        
    return (i-1) * N

T = int(input())
for t in range(1, T+1):
    N = int(input())
    print("Case #{}: {}".format(t, count_sheep(N)))