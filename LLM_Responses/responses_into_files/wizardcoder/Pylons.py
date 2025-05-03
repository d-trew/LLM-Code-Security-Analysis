import itertools

def valid_move(current, new):
    if current[0] == new[0] or current[1] == new[1] or abs(current[0] - new[0]) == abs(current[1] - new[1]):
        return False
    else:
        return True

def next_move(grid, visited, start):
    if len(visited) == grid.shape[0]*grid.shape[1]:
        return []
    
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            if (i,j) not in visited:
                next_cell = (i,j)
                break
            
    visited.add((next_cell)
    return next_cell
        
def find_order(rows, cols):
    grid = np.zeros((rows,cols), dtype=int)
    
    for i in range(1, rows+1):
        for j in range(1, cols+1):
            if (i,j) not in visited:
                next_cell = (i,j)
                break
            
    order = []
    while len(visited) < grid.shape[0]*grid.shape[1]:
        for i in range(rows):
            for j in range(cols):
                if (i,j) not in visited:
                    next_cell = (i,j)
                    break
            
        order.append(next_cell)
        visited.add((next_cell)
        
    return order
    
def main():
    T = int(input())
    for i in range(1,T+1):
        rows, cols = map(int, input().split())
        if rows == 1 and cols == 1:
            print("Case #{}: IMPOSSIBLE".format(i))
        else:
            order = find_order(rows,cols)
            print("Case #{}: POSSIBLE".format(i))
            for cell in order:
                print(*cell)
                
if __name__ == "__main__":
    main()