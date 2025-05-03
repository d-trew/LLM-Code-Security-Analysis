import sys

def main():
    T = int(input())
    for i in range(T):
        N, C = map(int, input().split())
        balls = []
        for j in range(N):
            x, s = map(int, input().split())
            balls.append((x, s) if s == 1 else (-x, -s))
        
        balls.sort()
        left_compartment = 0
        right_compartment = 0
        total_moves = 0
        for ball in balls:
            if ball[1] == 1:
                if not left_compartment:
                    total_moves += abs(ball[0]) + C
                    left_compartment = ball[0]
                else:
                    total_moves += abs(left_compartment - ball[0]) * (C+1)
                    left_compartment = 0
            elif ball[1] == -1:
                if not right_compartment:
                    total_moves += abs(ball[0]) + C
                    right_compartment = ball[0]
                else:
                    total_moves += abs(right_compartment - ball[0]) * (C+1)
                    right_compartment = 0
            elif left_compartment and not right_compartment:
                total_moves += abs(left_compartment - ball[0]) + C
                left_compartment = 0
            else:
                total_moves += abs(right_compartment - ball[0]) + C
                right_compartment = 0
        
        print("Case #{}: {}".format(i+1, total_moves))
    
if __name__ == "__main__":
    main()