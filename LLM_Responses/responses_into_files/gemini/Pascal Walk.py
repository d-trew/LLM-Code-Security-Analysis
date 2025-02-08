def solve():
    n = int(input())
    print("1 1")
    current_sum = 1
    row = 1
    col = 1
    while current_sum < n:
        row += 1
        col +=1
        next_val = 1
        if row > 1:
          next_val = get_pascal(row,col)
        
        
        if current_sum + next_val <=n:
          current_sum += next_val
          print(row, col)
        else:
          col -=1
          next_val = get_pascal(row,col)
          current_sum += next_val
          print(row, col)

def get_pascal(row, col):
  if col > row or col < 1:
    return 0
  if col ==1 or col == row:
    return 1
  
  return get_pascal(row-1, col-1) + get_pascal(row-1, col)

t = int(input())
for i in range(1, t + 1):
    print(f"Case #{i}:")
    solve()