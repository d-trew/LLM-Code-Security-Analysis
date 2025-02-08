def count_googlements(googlement):
    length = len(googlement)
    
    q = [googlement]
    visited = {googlement}
    count = 0
    
    while q:
        curr = q.pop(0)
        count +=1
        
        
        counts = [0] * length
        for digit in curr:
            counts[int(digit)] +=1

        next_googlement = "".join(map(str, counts))
        
        if next_googlement != curr and next_googlement not in visited:
            q.append(next_googlement)
            visited.add(next_googlement)

    return count


def solve():
    G = input()
    
    
    ans = 0
    q = [G]
    visited = {G}
    
    while q:
        curr = q.pop(0)
        
        is_original = True
        length = len(curr)
        
        
        counts = [0] * length
        for digit in curr:
            counts[int(digit)] +=1
        
        
        next_googlement = "".join(map(str, counts))
        
        if next_googlement != curr and next_googlement not in visited:
            q.append(next_googlement)
            visited.add(next_googlement)
        
        
        
        valid_original = True
        for digit in curr:
          if int(digit) > length:
            valid_original = False
            break

        if valid_original and all(c == '0' for c in curr) == False:
          ans+=1
          

    return ans


T = int(input())
for i in range(1, T + 1):
    result = solve()
    print(f"Case #{i}: {result}")