import sys

def solve():
    T = int(sys.stdin.readline())
    for _ in range(T):
        N, K = map(int, sys.stdin.readline().split())
        
        current_room = 1
        visited_edges = 0
        visited_rooms = {1}
        
        for _ in range(min(K, 8000)):
            R, P = map(int, sys.stdin.readline().split())
            current_room = R
            visited_edges += 1
            
            if P > 1:
                next_room = -1
                print("WALK")
                sys.stdout.flush()

                R_next, P_next = map(int, sys.stdin.readline().split())
                visited_rooms.add(R_next)
                visited_edges +=1

            
        estimate = (visited_edges * N) / (2 * len(visited_rooms))  #simple estimation
        print(f"ESTIMATE {int(estimate)}")
        sys.stdout.flush()

solve()