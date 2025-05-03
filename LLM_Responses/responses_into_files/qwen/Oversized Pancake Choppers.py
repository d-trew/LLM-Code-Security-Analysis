def min_cuts(slices, diners):
    from collections import Counter
    from math import gcd
    
    def reduce_angle(angle):
        d = gcd(angle, 360 * 10**9)
        return angle // d
    
    angles = [reduce_angle(slice) for slice in slices]
    counter = Counter(angles)
    
    cuts_needed = 0
    while len(counter) > diners:
        most_common = counter.most_common(2)
        if most_common[0][1] == most_common[1][1]:
            angle, count = most_common[0]
            new_angle = angle // 2
            counter[new_angle] += count
            cuts_needed += 1
        else:
            break
    
    return cuts_needed

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    T = int(data[index])
    index += 1
    results = []
    
    for _ in range(T):
        N = int(data[index])
        index += 1
        D = int(data[index])
        index += 1
        slices = list(map(int, data[index:index+N]))
        index += N
        
        result = min_cuts(slices, D)
        results.append(f"Case #{_ + 1}: {result}")
    
    for result in results:
        print(result)

if __name__ == "__main__":
    solve()