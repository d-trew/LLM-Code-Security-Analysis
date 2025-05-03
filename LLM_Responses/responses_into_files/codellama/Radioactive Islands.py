import math

def get_minimum_radiation(N, A, B, C):
    # Calculate the distance between each pair of islands
    distances = []
    for i in range(len(C)):
        for j in range(i + 1, len(C)):
            distances.append(math.sqrt((C[i] - C[j]) ** 2))

    # Calculate the total radiation received from each island
    total_radiation = []
    for i in range(len(distances)):
        total_radiation.append(distances[i] - 2)

    # Calculate the minimum total radiation dose
    min_dose = 0
    for i in range(len(total_radiation)):
        min_dose += total_radiation[i]

    return min_dose

if __name__ == "__main__":
    T = int(input())
    for t in range(T):
        N, A, B = map(float, input().split())
        C = list(map(float, input().split()))
        print("Case #{}: {}".format(t + 1, get_minimum_radiation(N, A, B, C)))