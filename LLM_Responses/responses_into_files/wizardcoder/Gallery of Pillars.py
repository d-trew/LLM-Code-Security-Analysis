import math

def is_visible(x, y, r):
    if x == 0 and y == 0:
        return False
    elif x < 0 or y < 0:
        return True
    else:
        return (r**2 >= x**2 + y**2)

def main():
    T = int(input())
    
    for i in range(1, T+1):
        N, R = map(int, input().split())
        
        count_visible = 0
        for j in range(N-1):
            for k in range(N-1):
                if is_visible(j+0.5, k+0.5, R/1e6) and is_visible(-j+0.5, -k+0.5, R/1e6) and is_visible(-j+0.5, k+0.5, R/1e6) and is_visible(j+0.5, -k+0.5, R/1e6):
                    count_visible += 1
        
        print("Case #{}: {}".format(i, count_visible))
    
if __name__ == "__main__":
    main()