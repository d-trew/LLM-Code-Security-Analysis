def solve():
    C, J = input().split()
    n = len(C)
    
    best_diff = float('inf')
    best_C = ""
    best_J = ""

    for i in range(10**C.count('?')):
        c_temp = list(C)
        c_num = i
        for j in range(n - 1, -1, -1):
            if c_temp[j] == '?':
                c_temp[j] = str(c_num % 10)
                c_num //= 10
        c_str = "".join(c_temp)
        c_int = int(c_str)

        for k in range(10**J.count('?')):
            j_temp = list(J)
            j_num = k
            for l in range(n - 1, -1, -1):
                if j_temp[l] == '?':
                    j_temp[l] = str(j_num % 10)
                    j_num //= 10
            j_str = "".join(j_temp)
            j_int = int(j_str)

            diff = abs(c_int - j_int)
            if diff < best_diff:
                best_diff = diff
                best_C = c_str
                best_J = j_str
            elif diff == best_diff:
                if c_int < int(best_C):
                    best_C = c_str
                    best_J = j_str
                elif c_int == int(best_C) and j_int < int(best_J):
                    best_J = j_str

    return best_C, best_J

T = int(input())
for i in range(1, T + 1):
    c, j = solve()
    print(f"Case #{i}: {c} {j}")