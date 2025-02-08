MOD = 1000000007

def solve():
    N, M, L = map(int, input().split())
    A = list(map(int, input().split()))
    
    total_score = 0
    
    for i in range(M**N):
        card_values = {}
        temp = i
        for j in range(N):
            card_values[j+1] = (temp % M) + 1
            temp //= M

        current_board = A[:]
        current_player = 0 # 0 for Alice, 1 for Bob

        for turn in range(L):
            if current_player == 0: #Alice's turn
                left_half = current_board[:len(current_board)//2]
                right_half = current_board[len(current_board)//2:]
                
                if max(card_values[x] for x in left_half) > max(card_values[x] for x in right_half):
                    current_board = left_half
                else:
                    current_board = right_half
            else: #Bob's turn
                left_half = current_board[:len(current_board)//2]
                right_half = current_board[len(current_board)//2:]
                
                if min(card_values[x] for x in left_half) < min(card_values[x] for x in right_half):
                    current_board = left_half
                else:
                    current_board = right_half
            current_player = 1 - current_player

        total_score = (total_score + card_values[current_board[0]]) % MOD
    return total_score

T = int(input())
for i in range(1, T + 1):
    result = solve()
    print(f"Case #{i}: {result}")