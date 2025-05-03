import heapq

def euclidean_distance(x1, y1, x2, y2):
    return (x1 - x2) ** 2 + (y1 - y2) ** 2

def find_closest_sweet(child_pos, sweets, taken_sweets):
    min_heap = []
    for sweet in sweets:
        if sweet not in taken_sweets:
            distance = euclidean_distance(child_pos[0], child_pos[1], sweet[0], sweet[1])
            heapq.heappush(min_heap, (distance, sweet))
    return min_heap

def can_save_blueberry_jelly(N, children, sweets):
    blueberry_jelly = sweets[0]
    taken_sweets = set()
    result = []
    
    for i in range(1, N + 2):
        closest_sweet = None
        closest_distance = float('inf')
        
        for child in children:
            if child not in taken_sweets:
                heap = find_closest_sweet(child, sweets, taken_sweets)
                while heap and heap[0][1] in taken_sweets:
                    heapq.heappop(heap)
                
                if heap and heap[0][0] < closest_distance:
                    closest_distance = heap[0][0]
                    closest_sweet = child
        
        if closest_sweet is None:
            return "IMPOSSIBLE"
        
        result.append((closest_sweet, blueberry_jelly))
        taken_sweets.add(blueberry_jelly)
    
    return "POSSIBLE\n" + "\n".join(f"{a} {b}" for a, b in result)

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    T = int(data[index])
    index += 1
    
    results = []
    
    for _ in range(T):
        N = int(data[index])
        index += 1
        
        children = []
        for _ in range(N):
            X = int(data[index])
            Y = int(data[index + 1])
            children.append((X, Y))
            index += 2
        
        sweets = []
        for _ in range(N + 1):
            X = int(data[index])
            Y = int(data[index + 1])
            sweets.append((X, Y))
            index += 2
        
        result = can_save_blueberry_jelly(N, children, sweets)
        results.append(result)
    
    for i, result in enumerate(results, start=1):
        print(f"Case #{i}: {result}")

if __name__ == "__main__":
    main()