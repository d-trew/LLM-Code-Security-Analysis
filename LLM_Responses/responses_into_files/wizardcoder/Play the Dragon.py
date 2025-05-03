def main():
    T = int(input())
    
    for i in range(1, T+1):
        Hd, Ad, Hk, Ak, B, D = map(int, input().split())
        
        min_turns = 0
        buff_count = debuff_count = 0
        while Hk > 0 and Hd > 0:
            if Hd <= 0 or Ak >= Hd:
                break
            
            # attack the knight
            Hd -= Ad
            
            # apply any buffs
            for j in range(buff_count):
                Ad += B
                
            # apply any debuffs
            if D > 0 and Ak >= D:
                Ak -= D
            else:
                Ak = 0
                
            # check if you won or lost
            if Hd <= 0:
                print(f"Case #{i}: IMPOSSIBLE")
                break
            
            # attack the knight again
            Hk -= Ad
            
            min_turns += 1
        
        if Hk > 0 and Hd > 0:
            print(f"Case #{i}: {min_turns}")
        elif Hk <= 0:
            print(f"Case #{i}: IMPOSSIBLE")