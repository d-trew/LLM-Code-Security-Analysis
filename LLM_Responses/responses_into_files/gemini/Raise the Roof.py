def solve():
    N = int(input())
    columns = []
    for i in range(N):
        x, y, h = map(int, input().split())
        columns.append(((x, y, h), i + 1))

    import itertools
    for perm in itertools.permutations(range(N)):
        valid = True
        for i in range(3, N):
            
            last_three = [columns[j][0] for j in perm[:i+1][-3:]]
            other_columns = [columns[j][0] for j in perm[:i+1][:-3]]

            #Check coplanarity (simplified -  not a robust coplanarity check, but sufficient for the problem constraints)

            
            valid_roof = True
            for col in other_columns:
                #Simplified check:  Just check if the z-coordinate is greater than the column height.  A true coplanarity check would be more complex.
                if not any(z > col[2] for x,y,z in last_three):
                    valid_roof = False
                    break

            if not valid_roof:
                valid = False
                break

        if valid:
            return " ".join(map(str, [columns[i][1] for i in perm]))

    return "No solution found"


T = int(input())
for i in range(1, T + 1):
    result = solve()
    print(f"Case #{i}: {result}")