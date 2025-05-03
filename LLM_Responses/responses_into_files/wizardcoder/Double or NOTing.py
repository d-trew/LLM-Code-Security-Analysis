from collections import deque
def main():
    T = int(input())
    
    for i in range(1, T+1):
        S, E = input().split()
        
        if len(S) > 8 or len(E) > 8 or (len(S) == 1 and S[0] != '0') or (len(E) == 1 and E[0] != '0'):
            print("Case #{}: IMPOSSIBLE".format(i))
        else:
            queue = deque()
            queue.append((S, 0))
            
            while queue:
                s, count = queue.popleft()
                
                if s == E:
                    print("Case #{}: {}".format(i, count)
                        break
                    
                for operation in ["NOT", "DOUBLE"]:
                    new_s = apply_operation(s, operation)
                    if new_s not in queue and len(new_s) <= 8:
                        queue.append((new_s, count+1))
                        
            else:
                print("Case #{}: IMPOSSIBLE".format(i))
                    
def apply_operation(binary, operation):
    binary = int(binary, 2)
    if operation == "NOT":
        return format(~binary & ((1 << len(binary)), 'b')
    elif operation == "DOUBLE":
        return format((binary<<1), 'b')
    
if __name__ == "__main__":
    main()