import heapq

def police_station_assignment(R, C, S, stations):
    # Create a grid of zeros representing the city
    grid = [[0] * C for _ in range(R)]

    # Assign blocks to stations
    for ri, ci, di in stations:
        for r in range(max(1, ri-di), min(R, ri+di+1)):
            for c in range(max(1, ci-di), min(C, ci+di+1)):
                if abs(r-ri) + abs(c-ci) <= di:
                    grid[r][c] = 1

    # Calculate the number of blocks assigned to each station
    assignments = [0] * S
    for r in range(R):
        for c in range(C):
            if grid[r][c]:
                ri, ci, _ = stations[grid[r][c]-1]
                assignments[grid[r][c]-1] += 1

    # Calculate the minimum and maximum number of blocks assigned to each station
    min_assignment = min(assignments)
    max_assignment = max(assignments)

    # Return the difference between the maximum and minimum number of blocks assigned
    return max_assignment - min_assignment

def main():
    T = int(input())
    for t in range(1, T+1):
        R, C, S = map(int, input().split())
        stations = []
        for _ in range(S):
            ri, ci, di = map(int, input().split())
            stations.append((ri, ci, di))
        print(f"Case #{t}: {police_station_assignment(R, C, S, stations)}")

if __name__ == "__main__":
    main()