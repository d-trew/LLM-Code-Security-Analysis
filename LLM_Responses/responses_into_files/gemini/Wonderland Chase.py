def solve():
    J, C, A, Q = map(int, input().split())
    edges = []
    for _ in range(C):
        u, v = map(int, input().split())
        edges.append((u, v))
        edges.append((v, u))

    adj = {i: [] for i in range(1, J + 1)}
    for u, v in edges:
        adj[u].append(v)

    def is_caught(alice_pos, queen_pos):
        return alice_pos == queen_pos

    def get_moves(current_pos, adj):
        return [current_pos] + adj[current_pos]

    def can_escape(alice_pos, queen_pos, max_moves):
        
        for _ in range(max_moves):
            #Queen's turn
            best_queen_move = -1
            min_moves_to_catch = float('inf')

            for next_queen_move in get_moves(queen_pos,adj):
                
                #Alice's turn
                best_alice_move = -1
                max_moves_to_avoid_catch = -1

                for next_alice_move in get_moves(alice_pos,adj):
                    if not is_caught(next_alice_move, next_queen_move):
                        
                        if max_moves_to_avoid_catch < 1 :
                            max_moves_to_avoid_catch = 1
                            best_alice_move = next_alice_move
                        

                if best_alice_move == -1: #Alice is caught
                    min_moves_to_catch = min(min_moves_to_catch,1)
                    
                    
                    break
                else:
                    alice_pos = best_alice_move
                    queen_pos = next_queen_move


        if is_caught(alice_pos, queen_pos):
          return False, 0
        else:
          return True, 0


    escaped, moves = can_escape(A, Q, 10**9)

    if escaped:
        return "SAFE"
    else:
        return moves


T = int(input())
for i in range(1, T + 1):
    result = solve()
    print(f"Case #{i}: {result}")