def find_stall(N, K):
    if N == 1:
        return (0, 0)
    elif N == 2:
        return (1, 0)
    else:
        stalls = [0] * (N + 2)
        stalls[0], stalls[N + 1] = -1, -1
        left, right = 1, N
        for _ in range(K):
            mid = (left + right) // 2
            if mid == left:
                left += 1
            elif mid == right:
                right -= 1
            else:
                if stalls[mid - 1] < stalls[mid + 1]:
                    left = mid
                else:
                    right = mid
        LS, RS = min(mid - stalls[left], stalls[right] - mid), max(stalls[left] - mid, mid - stalls[right])
        return (max(LS, RS), min(LS, RS))

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    T = int(data[0])
    index = 1
    results = []
    for _ in range(T):
        N = int(data[index])
        K = int(data[index + 1])
        index += 2
        result = find_stall(N, K)
        results.append(f"Case #{_+1}: {result[0]} {result[1]}")
    print("\n".join(results))

if __name__ == "__main__":
    main()