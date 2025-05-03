def main():
    T = int(input())
    for i in range(T):
        R, B, C = map(int, input().split())
        M = [list(map(int, input().split())) for _ in range(C)]
        
        # Sort the cashiers by their payment time (P) and then scan time (Si). This ensures that we allocate the bits to the cashier with the lowest P first.