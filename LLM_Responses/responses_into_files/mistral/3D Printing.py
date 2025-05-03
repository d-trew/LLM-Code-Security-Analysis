from collections import defaultdict
import sys
input = sys.stdin.readline

def main():
    t = int(input())
    for _ in range(t):
        c, m, y, k = map(int, input().split())
        total_ink = 10**6
        ink_needed = defaultdict(int)
        ink_needed['cyan'] = total_ink // 3 if c >= total_ink // 3 else c
        ink_needed['magenta'] = total_ink // 3 if m >= total_ink // 3 else m
        ink_needed['yellow'] = total_ink // 3 if y >= total_ink // 3 else y
        ink_needed['black'] = k if k >= total_ink - sum(ink_needed.values()) else total_ink - sum(ink_needed.values())

        if all([ink_needed[color] <= ci for color, ci in zip(ink_needed, (c, m, y, k))]):
            print(f'Case #{_+1}: {list(ink_needed.values())}')
        else:
            print(f'Case #{_+1}: IMPOSSIBLE')

if __name__ == '__main__':
    main()


This Python code reads the number of test cases and iterates through each one, calculating the ink needed for each color based on the total amount of ink required (10^6 units) and the ink available in each printer. It uses a defaultdict to store the ink needed for each color. If the ink needed for each color is less than or equal to the ink available in each respective printer, it prints the color combination. Otherwise, it prints IMPOSSIBLE for that test case.