def main():
    T = int(input())
    for t in range(T):
        U = int(input())
        records = []
        
        for i in range(104):
            M, Ri = input().split()
            if M == '-1':
                M = None
            else:
                M = int(M)
            records.append((M, Ri))
            
        D = recover_digit_string(records, U)
        print("Case #{}: {}".format(t+1, ''.join(D))
        
def recover_digit_string(records, U):
    digit_map = [None] * 10
    
    for i in range(104):
        M, Ri = records[i]
        if not M:
            continue
        for j, c in enumerate(Ri):
            if digit_map[j]:
                if c != digit_map[j]:
                    return None # Conflict found
            else:
                digit_map[j] = c
    
    for i in range(104):
        M, Ri = records[i]
        if not M:
            continue
        
        if len(Ri) != 5:
            return None # Invalid response length
        
        if not all(c.isupper() and c.isalpha() for c in Ri):
            return None # Non-letter character found
        
        mapping = {}
        for j, c in enumerate(Ri):
            if c not in mapping:
                mapping[c] = digit_map[j]
                
    for i in range(104):
        M, Ri = records[i]
        if not M:
            continue
        
        base10_str = ''.join([mapping[c] for c in Ri])
        if int(base10_str) < 1 or int(base10_str) > U:
            return None # Out-of-range response found
    
    return digit_map

# Read input from file
with open('input.txt', 'r') as f:
    T = int(f.readline())
    for t in range(T):
        U = int(f.readline().strip())
        records = []
        
        for i in range(104):
            M, Ri = f.readline().split()
            if M == '-1':
                M = None
            else:
                M = int(M)
            records.append((M, Ri))
            
        D = recover_digit_string(records, U)
        print("Case #{}: {}".format(t+1, ''.join(D), file=open('output.txt', 'a'))