from scipy.spatial import ConvexHull
import numpy as np

def build_order(columns):
    hulls = []
    for i, column in enumerate(columns):
        points = [column[:2]] + [columns[j][:2] for j in range(i)]
        hull = ConvexHull(np.array(points))
        if hull.status == 1:
            return "Case #{}: {}".format(len(hulls) + 1, list(range(i+1)))
        else:
            hulls.append((i, hull))

    for i, (idx, hull) in enumerate(reversed(hulls)):
        points = [column[:2] for column in columns[idx-3:]]
        hull_points = np.array([points[0]] + [point.tolist() for point in hull.vertices[1:]])
        while len(points) > 3:
            new_point = np.mean(hull_points, axis=0)
            if all((new_point - point).dot(new_point - points[i]) <= 0 for i in range(len(points))):
                break
            hull_points = np.insert(hull_points, 0, new_point)
        if len(points) > 3:
            return "Case #{}: {}".format(i+1, list(range(idx-2, idx)))
    return "Case #{}: {}".format(1, list(range(len(columns))))

T = int(input())
for _ in range(T):
    N = int(input())
    columns = []
    for _ in range(N):
        x, y, h = map(int, input().split())
        columns.append((x, y, h))
    print(build_order(columns))