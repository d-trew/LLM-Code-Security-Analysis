def solve():
    N_str = input()
    N = int(N_str)
    
    A_str = ""
    B_str = ""
    
    for digit in N_str:
        if digit == '4':
            A_str += '2'
            B_str += '2'
        else:
            A_str += digit
            B_str += '0'

    A = int(A_str)
    B = int(B_str)
    return A, B


T = int(input())
for i in range(1, T + 1):
    A, B = solve()
    print(f"Case #{i}: {A} {B}")