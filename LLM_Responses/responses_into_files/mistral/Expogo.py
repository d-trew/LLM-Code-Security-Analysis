t = int(input())
for _ in range(t):
    x, y = map(int, input().split())
    directions = []
    if y < 0:
        steps_to_goal_y = abs(y)
        while steps_to_goal_y > 0:
            if x > 0 and (steps_to_goal_y & 1 or not (x & 1)):
                directions.append('E')
                x -= 2
            elif x < 0 and (steps_to_goal_y & 1 or not (-x & 1)):
                directions.append('W')
                x += 2
            else:
                if steps_to_goal_y & 1:
                    directions.append('N' if y > 0 else 'S')
                    break
                else:
                    directions.append('S' if y > 0 else 'N')
                    break
            steps_to_goal_y //= 2
        while x:
            directions.append('E' if x > 0 else 'W')
            x = -x // 2
    elif y > 0:
        steps_to_goal_y = y
        while steps_to_goal_y > 0:
            if x < 0 and (steps_to_goal_y & 1 or not (-x & 1)):
                directions.append('E')
                x += 2
            elif x > 0 and (steps_to_goal_y & 1 or not (x & 1)):
                directions.append('W')
                x -= 2
            else:
                if steps_to_goal_y & 1:
                    directions.append('S' if y > 0 else 'N')
                    break
                else:
                    directions.append('N' if y > 0 else 'S')
                    break
            steps_to_goal_y //= 2
        while x:
            directions.append('W' if x < 0 else 'E')
            x = -x // 2
    print(f"Case #{_+1}: {'IMPOSSIBLE' if not directions else ''.join(directions)}")