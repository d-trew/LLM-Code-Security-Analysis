import sys
from collections import deque
input = sys.stdin.readline
R, T = map(int, input().split())
for _ in range(T):
 dartboard_radius, x, y = map(int, input().split())
 dartboard_center_x, dartboard_center_y = dartboard_radius * 2 + x, dartboard_radius * 2 + y
 wall = [[0] * 2100 for _ in range(2100)]
 q = deque([(dartboard_center_x, dartboard_center_y)])
 visited = {(dartboard_center_x, dartboard_center_y)}
 max_distance = R * R + (R - 1)**2
 for _ in range(300):
 x, y = q.popleft()
 if (x, y) == (0, 0):
 print("CENTER")
 break
 if (x, y) not in visited or max_distance < wall[x][y]:
 continue
 visited.add((x, y))
 wall[x][y] = len(visited)
 for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
 nx, ny = x + dx * R, y + dy * R
 if 0 <= nx < 2100 and 0 <= ny < 2100:
 q.append((nx, ny))
 else:
 continue
 if wall[nx][ny] != 0 and wall[nx][ny] <= max_distance:
 print(f"{dx * R + x} {dy * R + y}")


This code reads the number of test cases and the radius range from the standard input, then processes each test case up to 300 exchanges. The dartboard center is calculated based on the given radius and position. A 2D array `wall` represents the wall, with all points initially set to 0. The dartboard area and visited points are stored in a queue and a set respectively. The maximum distance from the center of the dartboard to any point on it is calculated. For each exchange, if the current position is the center of the dartboard, it prints "CENTER" and breaks. If the current position has already been visited or is further than the maximum distance from the center of the dartboard, it continues to the next iteration. Otherwise, it marks the current position as visited, adds the 4 neighboring points (if they are within the wall bounds) to the queue, and prints the x and y coordinates of the neighboring point if it is not already visited or has a smaller distance from the center of the dartboard than the maximum distance.