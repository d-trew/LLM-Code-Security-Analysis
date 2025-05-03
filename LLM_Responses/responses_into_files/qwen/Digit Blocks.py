import sys
from random import randint

def main():
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    T = int(data[index])
    N = int(data[index + 1])
    B = int(data[index + 2])
    P = int(data[index + 3])
    index += 4
    
    total_score = 0
    towers = [[] for _ in range(N)]
    
    for _ in range(T):
        for _ in range(N * B):
            D = int(data[index])
            index += 1
            
            best_tower = -1
            best_value = -1
            
            for i in range(N):
                if len(towers[i]) == B:
                    continue
                
                value = int(''.join(str(digit) for digit in towers[i][::-1]))
                if value > best_value:
                    best_value = value
                    best_tower = i
            
            if best_tower == -1:
                print(-1)
                return
            
            towers[best_tower].append(D)
        
        current_score = sum(int(''.join(str(digit) for digit in tower[::-1])) for tower in towers)
        total_score += current_score
        
        if total_score >= P:
            print(1)
        else:
            print(-1)

if __name__ == "__main__":
    main()