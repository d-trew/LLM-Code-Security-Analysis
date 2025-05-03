import math

def main():
    T = int(input())
    
    for t in range(1, T+1):
        N, D = map(int, input().split())
        A = list(map(float, input().split()))
        
        def angle_to_area(angle):
            return 0.5 * math.sin(math.radians(angle)) + 0.5
        
        total_area = sum([angle_to_area(a) for a in A])
        min_cuts = float('inf')
        
        for i in range(1, len(A)+1):
            if D*i > N:
                continue
            
            target_area = total_area / (D*i)
            cuts = 0
            current_angle = A[0]
            
            while angle_to_area(current_angle) < target_area and i <= len(A):
                cuts += 1
                current_angle -= min(current_angle, sum(A[i:]) / (len(A)-i))
                
            min_cuts = min(min_cuts, cuts)
            
        print("Case #{}: {}".format(t, min_cuts))
        
if __name__ == "__main__":
    main()