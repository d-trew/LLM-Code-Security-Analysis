def solve():
    N = int(input())
    S = input()
    B = list(map(int, input().split()))
    
    unknown_count = S.count('?')
    
    MOD = 1000000007
    
    count = 0
    
    for i in range(2**unknown_count):
        temp_S = list(S)
        binary = bin(i)[2:].zfill(unknown_count)
        k=0
        for j in range(N):
            if temp_S[j] == '?':
                temp_S[j] = 'C' if binary[k] == '1' else '.'
                k+=1
        
        boxes = list(temp_S)
        
        for j in range(N):
            if boxes[j] == 'C':
                dest = B[j]-1
                if boxes[dest] == '.':
                    boxes[dest] = 'C'
                    boxes[j] = '.'
        
        if boxes[N-1] == 'C':
            count = (count + 1) % MOD
            
    return count

T = int(input())
for i in range(1, T + 1):
    result = solve()
    print(f"Case #{i}: {result}")