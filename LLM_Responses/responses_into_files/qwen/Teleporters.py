from collections import deque

def min_teleportations(thundera, care_lot, teleporters):
    queue = deque([(thundera, 0)])
    visited = set()
    visited.add(thundera)
    
    while queue:
        current, steps = queue.popleft()
        
        if current == care_lot:
            return steps
        
        for teleporter in teleporters:
            distance = sum(abs(a - b) for a, b in zip(current, teleporter))
            new_positions = [(teleporter[0] + dx, teleporter[1] + dy, teleporter[2] + dz)
                             for dx, dy, dz in [(-distance, 0, 0), (distance, 0, 0),
                                               (0, -distance, 0), (0, distance, 0),
                                               (0, 0, -distance), (0, 0, distance)]]
            for new_pos in new_positions:
                if new_pos not in visited:
                    visited.add(new_pos)
                    queue.append((new_pos, steps + 1))
    
    return "IMPOSSIBLE"

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
        
        thundera = tuple(map(int, data[index:index+3]))
        index += 3
        
        care_lot = tuple(map(int, data[index:index+3]))
        index += 3
        
        teleporters = [tuple(map(int, data[index:index+3])) for _ in range(N)]
        index += N
        
        result = min_teleportations(thundera, care_lot, teleporters)
        results.append(result)
    
    for i, result in enumerate(results):
        print(f"Case #{i + 1}: {result}")

if __name__ == "__main__":
    main()