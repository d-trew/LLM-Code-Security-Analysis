import math

def max_perimeter(N, P, cookies):
    def perimeter(w, h):
        return 2 * (w + h)

    total_perimeter = sum(perimeter(w, h) for w, h in cookies)
    
    if total_perimeter <= P:
        return total_perimeter
    
    best_perimeter = total_perimeter
    for i in range(N):
        w, h = cookies[i]
        area = w * h
        for new_w in range(1, w):
            new_h = area // new_w
            if new_w * new_h == area:
                new_cookies = cookies[:i] + [(new_w, new_h), (w - new_w, h)] + cookies[i+1:]
                new_perimeter = total_perimeter - perimeter(w, h) + 2 * (new_w + new_h)
                if new_perimeter <= P and new_perimeter > best_perimeter:
                    best_perimeter = new_perimeter
    
    return best_perimeter

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    T = int(data[0])
    index = 1
    results = []
    
    for _ in range(T):
        N = int(data[index])
        P = int(data[index + 1])
        cookies = [(int(data[index + 2 + i * 2]), int(data[index + 3 + i * 2])) for i in range(N)]
        index += 2 * N + 2
        result = max_perimeter(N, P, cookies)
        results.append(f"Case #{_+1}: {result:.6f}")
    
    print("\n".join(results))

if __name__ == "__main__":
    main()