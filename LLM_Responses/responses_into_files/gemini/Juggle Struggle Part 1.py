def cross_product(o, a, b):
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

def solve():
    N = int(input())
    jugglers = []
    for i in range(2 * N):
        x, y = map(int, input().split())
        jugglers.append((x, y))

    
    def check_magnificent(pairs):
        for i in range(N):
            for j in range(i + 1, N):
                p1 = pairs[i]
                p2 = pairs[j]
                
                if cross_product(jugglers[p1[0]], jugglers[p1[1]], jugglers[p2[0]]) * cross_product(jugglers[p1[0]], jugglers[p1[1]], jugglers[p2[1]]) > 0:
                    if cross_product(jugglers[p2[0]], jugglers[p2[1]], jugglers[p1[0]]) * cross_product(jugglers[p2[0]], jugglers[p2[1]], jugglers[p1[1]]) >0:
                        return False
        return True

    import itertools
    
    for pair_iter in itertools.permutations(range(2 * N), 2*N):
        pairs = []
        temp = list(pair_iter)
        for i in range(0,2*N,2):
            pairs.append((temp[i],temp[i+1]))

        is_magnificent = True
        
        for i in range(N):
            for j in range(i+1,N):
                if cross_product(jugglers[pairs[i][0]],jugglers[pairs[i][1]],jugglers[pairs[j][0]]) * cross_product(jugglers[pairs[i][0]],jugglers[pairs[i][1]],jugglers[pairs[j][1]]) >=0 :
                    if cross_product(jugglers[pairs[j][0]],jugglers[pairs[j][1]],jugglers[pairs[i][0]]) * cross_product(jugglers[pairs[j][0]],jugglers[pairs[j][1]],jugglers[pairs[i][1]]) >= 0:
                         is_magnificent = False
                         break
            if not is_magnificent:
                break
        
        if is_magnificent:
            result = ""
            for pair in pairs:
                result += str(pair[0] + 1) + str(pair[1] + 1)
            return result

T = int(input())
for i in range(1, T + 1):
    print(f"Case #{i}: {solve()}")