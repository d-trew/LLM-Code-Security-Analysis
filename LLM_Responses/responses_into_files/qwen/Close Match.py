def fill_scoreboard(C, J):
    min_diff = float('inf')
    best_C = C
    best_J = J

    for c in range(10**len(C)):
        for j in range(10**len(J)):
            C_filled = str(c).zfill(len(C))
            J_filled = str(j).zfill(len(J))
            diff = abs(int(C_filled) - int(J_filled))
            if diff < min_diff:
                min_diff = diff
                best_C = C_filled
                best_J = J_filled
            elif diff == min_diff:
                if int(C_filled) < int(best_C):
                    best_C = C_filled
                    best_J = J_filled
                elif int(C_filled) == int(best_C) and int(J_filled) < int(best_J):
                    best_C = C_filled
                    best_J = J_filled

    return best_C, best_J

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    T = int(data[0])
    results = []
    
    for i in range(1, 2*T+1, 2):
        C = data[i]
        J = data[i+1]
        best_C, best_J = fill_scoreboard(C, J)
        results.append(f"Case #{i//2 + 1}: {best_C} {best_J}")
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()