def main():
    T = int(input())
    for i in range(T):
        N, K = map(int, input().split())
        # initialize rooms with their number of passages
        rooms = [[] for _ in range(N)]
        for j in range(K+1):
            R, P = map(int, input().split())
            if j < K:
                for k in range(P):
                    room_to = int(input())
                    rooms[R-1].append(room_to) # subtract 1 to index from 0 to N-1
            else: # estimation operation
                E = estimate_passages(rooms, K)
                print(E)

def estimate_passages(rooms, K):
    passages = 0
    visited = set()
    for i in range(K+1):
        R, P = map(int, input().split())
        if i < K: # walk through a passage and visit the connected room
            room_to = random.choice(rooms[R-1]) # subtract 1 to index from 0 to N-1
            visited.add(room_to)
            passages += P - len(rooms[room_to-1]) + 1 # add number of new rooms visited minus the ones already visited
        else: # estimation operation
            return passages * 2 // 3, passages * 4 // 3

if __name__ == "__main__":
    main()