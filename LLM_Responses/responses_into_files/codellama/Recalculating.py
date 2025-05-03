import math

def main():
    test_cases = int(input())
    for case in range(test_cases):
        N, D = map(int, input().split())
        repair_centers = []
        for i in range(N):
            x, y = map(int, input().split())
            repair_centers.append((x, y))
        
        # Calculate the area of each red region
        red_region_area = 0
        for i in range(N):
            for j in range(i+1, N):
                distance = math.sqrt((repair_centers[i][0] - repair_centers[j][0])**2 + (repair_centers[i][1] - repair_centers[j][1])**2)
                if distance <= D:
                    red_region_area += 1
        
        # Calculate the area of each blue region
        blue_region_area = 0
        for i in range(N):
            for j in range(i+1, N):
                distance = math.sqrt((repair_centers[i][0] - repair_centers[j][0])**2 + (repair_centers[i][1] - repair_centers[j][1])**2)
                if distance > D:
                    blue_region_area += 1
        
        # Calculate the probability of Principia being in a red region
        prob_red = red_region_area / (N * (N - 1))
        
        # Calculate the probability of Principia being in a blue region
        prob_blue = blue_region_area / (N * (N - 1))
        
        # Find the minimum denominator
        min_denom = math.inf
        for i in range(N):
            for j in range(i+1, N):
                distance = math.sqrt((repair_centers[i][0] - repair_centers[j][0])**2 + (repair_centers[i][1] - repair_centers[j][1])**2)
                if distance <= D:
                    min_denom = min(min_denom, distance)
        
        # Calculate the probability of Principia being in a distinguishable location
        prob_distinguishable = (prob_red * min_denom) / (prob_red * min_denom + prob_blue * (D - min_denom))
        
        print(f"Case #{case+1}: {int(prob_distinguishable*100)}/{int((prob_distinguishable*100)%100)}")

if __name__ == "__main__":
    main()