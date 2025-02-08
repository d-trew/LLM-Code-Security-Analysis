def solve():
    N = int(input())
    words = [input() for _ in range(N)]
    
    ans = 0
    for i in range(1 << N):
        subset = []
        for j in range(N):
            if (i >> j) & 1:
                subset.append(words[j])

        if len(subset) % 2 != 0:
            continue

        
        possible = True
        
        if len(subset) > 0:
          
          
          
          
          
          used = [False] * len(subset)
          count = 0
          
          for k in range(len(subset)):
            if used[k]: continue
            found_pair = False
            for l in range(k + 1, len(subset)):
              if used[l]: continue
              
              
              rhymed = False
              for accent1 in range(len(subset[k])):
                for accent2 in range(len(subset[l])):
                  suffix1 = subset[k][accent1:]
                  suffix2 = subset[l][accent2:]
                  if suffix1 == suffix2:
                    rhymed = True
                    break
                if rhymed: break
              if rhymed:
                
                used[k] = True
                used[l] = True
                count +=2
                found_pair = True
                break
          ans = max(ans, count)

    return ans

T = int(input())
for i in range(1, T + 1):
    print(f"Case #{i}: {solve()}")