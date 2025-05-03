import heapq
def find_cart():
    T = int(input())
    for _ in range(T):
        P, Q = map(int, input().split())
        directions = {}
        for _ in range(P):
            x, y, direction = input().split()
            x, y = int(x), int(y)
            if direction == 'N':
                directions[(x, y + 1)] = directions.get((x, y + 1), 0) + 1
            elif direction == 'S':
                directions[(x, y - 1)] = directions.get((x, y - 1), 0) + 1
            elif direction == 'E':
                directions[(x + 1, y)] = directions.get((x + 1, y), 0) + 1
            elif direction == 'W':
                directions[(x - 1, y)] = directions.get((x - 1, y), 0) + 1
        min_heap = []
        for location, count in directions.items():
            if location[0] < Q and location[1] < Q:
                heapq.heappush(min_heap, (-count, *location))
        cart_location = None
        max_count = 0
        while min_heap:
            count, x, y = heapq.heappop(min_heap)
            if count > max_count:
                max_count = count
                cart_location = (x, y)
        print(f'Case #{_ + 1}: {cart_location[0]} {cart_location[1]}')