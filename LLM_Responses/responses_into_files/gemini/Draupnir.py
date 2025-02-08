def solve():
    T, W = map(int, input().split())
    for _ in range(T):
        rings = [0] * 6
        
        def query(day):
            print(day)
            return int(input())

        def count_rings(day, rings_counts):
            total_rings = 0
            for i in range(6):
                num_rings = rings_counts[i]
                for d in range(i, day + 1, i + 1):
                    total_rings += num_rings
                    num_rings *= 2
            return total_rings

        
        for i in range(W):
          day_to_query = i + 1 #Query different days. Adjust as needed for better accuracy.
          total_rings_on_day = query(day_to_query)

          if total_rings_on_day == -1:
            return

          rings_guess = list(rings)
          found = False
          for r0 in range(101):
              rings_guess[0] = r0
              for r1 in range(101):
                  rings_guess[1] = r1
                  for r2 in range(101):
                      rings_guess[2] = r2
                      for r3 in range(101):
                          rings_guess[3] = r3
                          for r4 in range(101):
                              rings_guess[4] = r4
                              for r5 in range(101):
                                  rings_guess[5] = r5
                                  if count_rings(day_to_query,rings_guess) % (10**9 + 7) == total_rings_on_day:
                                      rings = rings_guess
                                      found = True
                                      break
                              if found:
                                  break
                          if found:
                              break
                      if found:
                          break
                  if found:
                      break
              if found:
                  break

        print(*rings)


solve()