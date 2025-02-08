def solve():
    N, L = map(int, input().split())
    G = [input() for _ in range(N)]
    B = input()

    if any(B == g for g in G):
        return "IMPOSSIBLE"

    if all(g[0] == '0' for g in G) and B[0] == '1':
        return "1" + "?" * (L -1) + " " + "0" * (L-1)

    if all(g[0] == '1' for g in G) and B[0] == '0':
        return "0" + "?" * (L-1) + " " + "1" * (L-1)

    
    if all(b == '1' for b in B):
        prog1 = "1" + "?" * (L - 1)
        prog2 = "0" * (L - 1)
        
        
        possible = False
        for g in G:
          found = False
          for i in range(1 << (2*L - 2)):
            res = ""
            cur = 0
            p1_idx = 0
            p2_idx = 0
            for j in range(2 * L - 2):
              if (i >> j) & 1:
                if p1_idx < L-1:
                  if prog1[p1_idx+1] == '?':
                    cur = 1
                  else:
                    cur = int(prog1[p1_idx+1])
                  p1_idx += 1
                
              else:
                if p2_idx < L-1:
                  if prog2[p2_idx] == '0':
                    cur = 0
                  else:
                    cur = 1
                  p2_idx += 1
              
              res += str(cur)

            if res == g:
              found = True
              break
          if not found:
            possible = False
            break
          else:
            possible = True
        if possible:
          return prog1 + " " + prog2
        

    return "IMPOSSIBLE"


T = int(input())
for i in range(1, T + 1):
    result = solve()
    print(f"Case #{i}: {result}")