def main():
    T = int(input())
    for i in range(T):
        N, D = map(int, input().split())
        repair_centers = []
        for _ in range(N):
            x, y = map(float, input().split())
            repair_centers.append((x, y))
        
        # calculate area of each red square and blue section
        total_area = 0
        distinguishable_area = 0
        for rc in repair_centers:
            x, y = rc
            total_area += (2*D+1)**2 - (x-D)*(y-D) + (x+D)*(y+D) - (x+D)*(y-D) - (x-D)*(y+D)
        
        # calculate the probability of being deployed to a distinguishable point
        for rc in repair_centers:
            x, y = rc
            area_within_range = 2*(D+1)**2 - (x-D)*(y-D) + (x+D)*(y+D) - (x+D)*(y-D) - (x-D)*(y+D)
            distinguishable_area += area_within_range
        
        prob = float(distinguishable_area)/float(total_area)
        print("Case #{}: {} {}".format(i+1, int(prob*10**9))

if __name__ == "__main__":
    main()