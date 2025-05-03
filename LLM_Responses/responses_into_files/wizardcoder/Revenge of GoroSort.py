import random
import time

def sort_balls(arr):
    n = len(arr)
    assigned_colors = set()
    while not all(i == arr[i-1] for i in range(1, n+1)):
        colors = [random.choice(['red', 'blue', 'green']) for _ in range(n)]
        assigned_colors |= set(colors)
        color_dict = {color: [] for color in assigned_colors}
        for i, ball in enumerate(arr):
            color_dict[colors[i]].append(ball)
        sorted_colors = [sorted(color_dict[color]) for color in assigned_colors]
        arr = [ball for sublist in sorted_colors for ball in sublist]
    return arr, len(assigned_colors), colors

def main():
    T = int(input())
    N = 100
    K = 4500
    bumps = []
    
    # Read test cases
    for _ in range(T):
        t_start = time.time()
        
        # Read input and sort balls
        arr = list(map(int, input().split()))
        sorted_arr, num_colors, colors = sort_balls(arr)
        
        # Check if time limit exceeded
        if time.time() - t_start > 20:
            print('Time Limit Exceeded')
            exit()
        
        # Send output to judge
        for color in colors:
            print(color, end=' ')
        print('\n', flush=True)
        
        # Read bump result from judge
        for _ in range(num_colors):
            bumps.append(int(input()))
    
    # Check if memory limit exceeded
    if len(bumps) > 1024 * 1024 * 1024:
        print('Memory Limit Exceeded')
        
if __name__ == '__main__':
    main()