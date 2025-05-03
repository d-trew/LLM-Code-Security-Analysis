import math

def falling_balls(C, B):
    # Calculate the number of rows needed for the layout
    rows = math.ceil(math.log2(C)) + 1

    # Initialize the layout with no ramps
    layout = [['.' for _ in range(C)] for _ in range(rows)]

    # Add ramps to the left and right columns
    for i in range(1, rows):
        layout[i][0] = '/'
        layout[i][-1] = '\\'

    # Add balls to the bottom row
    for i, b in enumerate(B):
        layout[-1][i] = 'o'

    return layout

if __name__ == "__main__":
    T = int(input())
    for t in range(1, T+1):
        C = int(input())
        B = list(map(int, input().split()))
        layout = falling_balls(C, B)
        print(f"Case #{t}: {len(layout)}")
        for row in layout:
            print(''.join(row))