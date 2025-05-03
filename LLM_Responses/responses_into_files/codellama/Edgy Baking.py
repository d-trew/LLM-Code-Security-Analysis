import math
def closest_to(perimeters, P):
    total = 0
    for perimeter in perimeters:
        total += perimeter
    if total > P:
        return -1
    elif total == P:
        return total
    else:
        min_diff = math.inf
        closest = None
        for i in range(len(perimeters)):
            for j in range(i+1, len(perimeters)):
                new_total = total - perimeters[i] - perimeters[j] + 2 * (perimeters[i] + perimeters[j])
                if new_total <= P:
                    diff = abs(new_total - P)
                    if diff < min_diff:
                        closest = [i, j]
                        min_diff = diff
        if closest is None:
            return -1
        else:
            perimeters[closest[0]] /= 2
            perimeters[closest[1]] /= 2
            return total

if __name__ == "__main__":
    T = int(input())
    for t in range(T):
        N, P = map(int, input().split())
        cookies = []
        for _ in range(N):
            w, h = map(int, input().split())
            cookies.append((w,h))
        print("Case #" + str(t+1) + ": " + str(closest_to(cookies, P)))