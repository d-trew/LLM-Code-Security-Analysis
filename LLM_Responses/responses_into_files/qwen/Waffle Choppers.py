def can_divide_waffle(R, C, H, V, waffle):
    total_chips = sum(row.count('@') for row in waffle)
    pieces = (H + 1) * (V + 1)
    
    if total_chips % pieces != 0:
        return "IMPOSSIBLE"
    
    chip_per_piece = total_chips // pieces
    
    def is_divisible(start_row, end_row, start_col, end_col):
        chips_in_piece = sum(row[start_col:end_col].count('@') for row in waffle[start_row:end_row])
        return chips_in_piece == chip_per_piece

    # Check if all pieces have the same number of chocolate chips
    for i in range(H + 1):
        for j in range(V + 1):
            if not is_divisible(i * (R // (H + 1)), (i + 1) * (R // (H + 1)), j * (C // (V + 1)), (j + 1) * (C // (V + 1))):
                return "IMPOSSIBLE"
    
    return "POSSIBLE"

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    T = int(data[0])
    index = 1
    results = []
    
    for _ in range(T):
        R = int(data[index])
        C = int(data[index + 1])
        H = int(data[index + 2])
        V = int(data[index + 3])
        waffle = [data[index + 4 + i] for i in range(R)]
        index += 4 + R
        
        result = can_divide_waffle(R, C, H, V, waffle)
        results.append(result)
    
    for i, result in enumerate(results):
        print(f"Case #{i+1}: {result}")

if __name__ == "__main__":
    main()