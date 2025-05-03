def get_picture(X, Y, M):
    x = X
    y = Y
    moves = {"N": (0, -1), "E": (1, 0), "S": (0, 1), "W": (-1, 0)}
    
    for move in M:
        dx, dy = moves[move]
        x += dx
        y += dy
        
    return abs(x) + abs(y)
        
def main():
    T = int(input())
    
    for i in range(1, T+1):
        X, Y = map(int, input().split())
        M = input()
        
        if len(M) == 0:
            print("Case #{}: IMPOSSIBLE".format(i))
        else:
            result = get_picture(X, Y, M)
            
            if result <= max(abs(X), abs(Y)):
                print("Case #{}: {}".format(i, result))
            else:
                print("Case #{}: IMPOSSIBLE".format(i))
                
if __name__ == "__main__":
    main()