import sys

def max_speed(D, N, horses):
    def can_reach_destination(speed):
        for K, S in horses:
            time_to_meet = (D - K) / speed
            if time_to_meet <= 1:
                return False
            if K + S * time_to_meet > D:
                return False
        return True

    left, right = 0, 10**9
    while right - left > 1e-6:
        mid = (left + right) / 2
        if can_reach_destination(mid):
            left = mid
        else:
            right = mid
    return left

input = sys.stdin.read
data = input().split()

T = int(data[0])
index = 1
results = []

for _ in range(T):
    D = int(data[index])
    N = int(data[index + 1])
    horses = []
    index += 2
    for _ in range(N):
        K = int(data[index])
        S = int(data[index + 1])
        horses.append((K, S))
        index += 2

    result = max_speed(D, N, horses)
    results.append(f"Case #{_+1}: {result:.6f}")

for result in results:
    print(result)