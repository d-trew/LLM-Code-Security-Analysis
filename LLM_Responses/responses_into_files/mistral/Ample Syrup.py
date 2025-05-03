import sys
from math import pi

def solve(r_list, h_list, k):
    r_list.sort(reverse=True)
    h_list.sort(reverse=True)
    stack = []
    total_area = 0

    for i in range(k):
        max_radius = r_list[i]
        max_height = h_list[i]

        # Find the index of the next larger height
        j = i + 1
        while j < len(h_list) and h_list[j] <= max_height:
            j += 1

        if j == len(h_list):
            break

        top_area = 2 * pi * max_radius * min(max_height, h_list[j])
        side_area = 2 * pi * max_radius * (min(max_height, h_list[j]) - max_height)

        total_area += top_area + side_area

        stack.append((max_radius, max_height))
        r_list = [r for r in r_list if r != max_radius]
        h_list = [h for h in h_list if h != max_height and h >= max_height - max_height % (j - i)]

    return total_area

def main():
    T = int(input().strip())
    for t in range(1, T + 1):
        n, k = map(int, input().split())
        r_list, h_list = [], []
        for _ in range(n):
            r, h = map(float, input().split())
            r_list.append(r)
            h_list.append(h)
        print(f"Case #{t}: {solve(r_list, h_list, k)}")

if __name__ == "__main__":
    main()