import heapq

def solve():
    T = int(input())
    for _ in range(T):
        N = int(input())
        children = [(0, i) for i in range(1, N+2)] # (distance, id) tuple list for children and jelly
        sweets = [] # list for non-jelly sweets
        for _ in range(N):
            x, y = map(int, input().split())
            children.append((((x - children[0][0])**2 + (y - children[0][1])**2)**0.5, -1)) # calculate distance from jelly
            sweets.append((x, y))
        heapq.heapify(children) # sort children by distance from jelly

        order = []
        for _ in range(N):
            while len(sweets) > 0 and children[0][0] == 0: # if no sweet left or current child is at jelly, pop from heap
                heapq.heappop(children)
            if not sweets: break # if all sweets are taken by now
            child_id = children[0][1] + 1 # get id of the child with smallest distance to remaining sweets
            order.append((child_id, sweets[0][0], sweets[0][1])) # append child and the closest sweet to order list
            sweets[0] = (float('inf'), -1) # mark the picked sweet as unreachable
            for i, sweet in enumerate(sweets[1:]):
                if sweet != (float('inf'), -1): # check if there are remaining sweets
                    distance = ((sweet[0] - children[0][0])**2 + (sweet[1] - children[0][1])**2)**0.5
                    heapq.heappush(children, (distance, child_id)) # update distance of all remaining sweets to current child
            heapq.heappop(children) # pop the current child from heap
        if len(sweets) > 0: print("Case #{}: IMPOSSIBLE".format(_ + 1)) # check if any sweet is left after all children went
        else:
            for child in order: print("Case #{}: POSSIBLE".format(_ + 1))
            for child in order: print(*child)

solve()


This code reads the input, initializes the list of children and sweets, calculates distances from each child to all sweets (including the jelly), sorts the children by their distance to the jelly, and then simulates Mr. Jolly's calling order using a min-heap data structure. If there are remaining sweets after all children have gone, it means that Mr. Jolly cannot save his blueberry jelly, so it prints "IMPOSSIBLE". Otherwise, it prints "POSSIBLE" and the order in which the children will go and which sweets they will pick.