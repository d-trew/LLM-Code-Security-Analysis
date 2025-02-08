def solve():
    M = int(input())
    recipes = []
    for _ in range(M):
        recipes.append(list(map(int, input().split())))
    inventory = list(map(int, input().split()))

    def check(lead_amount):
        temp_inventory = list(inventory)
        temp_inventory[0] -= lead_amount
        
        for _ in range(100): # Iterate to allow for multiple recipe applications
          changed = False
          for i in range(M):
            if temp_inventory[i] < 0:
              needed = -temp_inventory[i]
              temp_inventory[i] += needed
              temp_inventory[recipes[i][0]-1] -= needed
              temp_inventory[recipes[i][1]-1] -= needed
              changed = True
          if not changed:
            break

        for amount in temp_inventory:
            if amount < 0:
                return False
        return True

    left = 0
    right = sum(inventory)
    ans = 0
    while left <= right:
        mid = (left + right) // 2
        if check(mid):
            ans = mid
            left = mid + 1
        else:
            right = mid - 1
    return ans

T = int(input())
for i in range(1, T + 1):
    result = solve()
    print(f"Case #{i}: {result}")