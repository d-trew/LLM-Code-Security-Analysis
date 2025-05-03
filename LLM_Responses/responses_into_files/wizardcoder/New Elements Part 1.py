import sys

def valid_orderings(molecules):
    n = len(molecules)
    count = 0
    
    for i in range(n):
        for j in range(i+1, n):
            if molecules[i][0] < molecules[j][0]:
                count += 1
            elif molecules[i][1] < molecules[j][1]:
                count += 1
    
    return count

def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        molecules = []
        
        for _ in range(n):
            c, j = map(int, input().split())
            molecules.append((c,j))
            
        print("Case #{}: {}".format(i+1, valid_orderings(molecules)))
    
if __name__ == "__main__":
    main()