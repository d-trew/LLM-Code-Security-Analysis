import sys
from itertools import combinations

def main():
    test_cases = int(input())
    
    for i in range(test_cases):
        n = int(input())
        
        jugglers = []
        pairs = []
        
        for _ in range(n*2):
            x, y = map(int, input().split())
            jugglers.append((x,y))
            
        for pair in combinations(jugglers, 2):
            if is_magnificent(pair[0], pair[1]):
                pairs.append(str(pair))
                
        print("Case #{}: {}".format(i+1), " ".join(pairs))
        
def is_magnificent(jug1, jug2):
    return abs(jug1[0] - jug2[0]) != abs(jug1[1] - jug2[1]) and abs(jug1[0] - jug2[0]) + abs(jug1[1] - jug2[1]) == 0
    
if __name__ == "__main__":
    main()