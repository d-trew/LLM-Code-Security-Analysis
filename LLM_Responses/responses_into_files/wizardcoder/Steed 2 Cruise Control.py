from math import sqrt

def main():
    T = int(input())
    
    for i in range(T):
        D, N = map(int, input().split())
        
        horses = []
        for j in range(N):
            K, S = map(int, input().split())
            horses.append((K, S))
            
        max_speed = 10**9
        min_speed = 0
        
        while abs(max_speed - min_speed) > 1e-6:
            mid_speed = (min_speed + max_speed) / 2.0
            if can_ride_at_speed(horses, D, mid_speed):
                min_speed = mid_speed
            else:
                max_speed = mid_speed
                
        print("Case #%d: %.6f" % (i+1, min_speed) if i > 0 else "Case #%d: %.6f" % (i+1, round(min_speed, 6)))
        
def can_ride_at_speed(horses, D, speed):
    time = 0.0
    
    for horse in horses:
        K, S = horse
        time += sqrt((D - K)**2 + (speed**2)) / S
        
    return time <= D

if __name__ == "__main__":
    main()