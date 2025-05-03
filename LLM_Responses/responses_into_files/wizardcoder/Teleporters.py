def main():
    T = int(input())
    
    for i in range(T):
        N = int(input())
        
        thundera = tuple(map(int, input().split()))
        care_a_lot = tuple(map(int, input().split()))
        teleporters = []
        
        for _ in range(N):
            teleporter = tuple(map(int, input().split())
            teleporters.append(teleporter)
            
        min_distance = float('inf')
        min_path = None
        
        for t1 in teleporters:
            for t2 in teleporters:
                if t1 == t2:
                    continue
                    
                distance = sum(abs(x1 - x2) + abs(y1 - y2) + abs(z1 - z2) for (x1, y1, z1), (x2, y2, z2) in [(thundera, t1), (t1, t2)] if t1 != thundera and t2 != care_a_lot)
                    
                if distance < min_distance:
                    min_distance = distance
                    min_path = [t1]
                    
        if sum(abs(x1 - x2) + abs(y1 - y2) + abs(z1 - z2) for (x1, y1, z1), (x2, y2, z2) in [(thundera, care_a_lot)]):
            print("Case #{}: {}".format(i+1, len(min_path)+1))
        else:
            print("Case #{}: IMPOSSIBLE".format(i+1))