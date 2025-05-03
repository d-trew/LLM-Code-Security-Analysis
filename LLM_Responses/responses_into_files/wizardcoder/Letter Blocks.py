def main():
    cases = int(input())
    for i in range(1, cases+1):
        num_towers = int(input())
        towers = []
        for j in range(num_towers):
            towers.append(input().strip())
        
        def is_valid(towers):
            for tower in towers:
                if len(set(tower)) != len(towers[0]):
                    return False
            
            for j in range(len(towers[0])):
                current = towers[0][j]
                for k in range(1, len(towers)):
                    if current != towers[k][j]:
                        return False
            for tower in towers:
                for j in range(len(tower)-1):
                    if tower[j] == current and tower[j+1] != current:
                        return False
            
            return True
        
        def build_mega_tower(towers):
            result = []
            for j in range(len(towers[0])):
                if is_valid([tower[:j+1] for tower in towers]):
                    result.append(towers[0][j])
                else:
                    break
            
            return "".join(result) if len(result) == num_towers*len(towers[0]) else "IMPOSSIBLE"
        
        print("Case #{}: {}".format(i, build_mega_tower(towers))