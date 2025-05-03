from queue import PriorityQueue

def solve():
    T = int(input())
    for t in range(T):
        N, A, B = map(int, input().split())
        units = list(map(int, input().split()))
        
        pq = PriorityQueue()
        for u in units:
            pq.put((u, 1))
            
        while not pq.empty():
            curr_unit, count = pq.get()
            if curr_unit <= A or (curr_unit - B) <= 0:
                continue
            new_units = [(curr_unit - x, count + 1) for x in range(A, min(B, curr_unit))]
            for nu, nc in new_units:
                pq.put((nu, nc))
        
        if not pq.empty():
            print("Case #{}: {}".format(t + 1, pq.get()[0]))
        else:
            print("Case #{}: IMPOSSIBLE".format(t + 1))
            
if __name__ == "__main__":
    solve()