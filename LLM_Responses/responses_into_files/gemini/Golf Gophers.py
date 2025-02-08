T, N, M = map(int, input().split())

def solve():
    for _ in range(T):
        gophers = 0
        for i in range(min(N, 10)):  # Adjust the number of nights based on time constraints
            blades = [2] * 18 # Start with 2 blades on each windmill
            print(*blades)
            results = list(map(int, input().split()))

            if results == [-1]:
                return

            total_rotation = sum(results)
            
            if i == 0:
                gophers = total_rotation
            else:
                gophers = total_rotation

        print(gophers)
        response = int(input())
        if response == -1:
            return

solve()