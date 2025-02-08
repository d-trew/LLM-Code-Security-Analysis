def solve():
    T, A, B = map(int, input().split())
    for _ in range(T):
        x, y = 0, 0
        print(x, y)
        response = input()
        if response == "CENTER":
            continue
        elif response == "WRONG":
            return
        
        #Binary Search for X and Y
        low_x = -10**9
        high_x = 10**9
        low_y = -10**9
        high_y = 10**9
        
        for _ in range(30): # Adjust iterations as needed
            mid_x = (low_x + high_x) // 2
            print(mid_x, y)
            response = input()
            if response == "CENTER":
                break
            elif response == "WRONG":
                return
            elif response == "HIT":
                low_x = mid_x
            else:
                high_x = mid_x

            mid_y = (low_y + high_y) // 2
            print(x, mid_y)
            response = input()
            if response == "CENTER":
                break
            elif response == "WRONG":
                return
            elif response == "HIT":
                low_y = mid_y
            else:
                high_y = mid_y
            
            x = (low_x + high_x) // 2
            y = (low_y + high_y) // 2

        print(x,y)
        response = input()
        if response != "CENTER":
            return

solve()