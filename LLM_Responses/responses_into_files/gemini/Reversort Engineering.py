def reversort_cost(arr):
    cost = 0
    for i in range(len(arr) - 1):
        j = arr.index(min(arr[i:]))
        arr[i:j+1] = arr[i:j+1][::-1]
        cost += (j - i + 1)
    return cost

def solve():
    N, C = map(int, input().split())
    
    min_cost = N - 1
    if C < min_cost:
        return "IMPOSSIBLE"
    
    if C == min_cost:
        return " ".join(map(str, list(range(1, N + 1))))

    
    for i in range(1 << (N -1 )):
        temp_arr = list(range(1,N+1))
        cost = 0
        current_cost = 0
        temp_list = []
        k=0

        for j in range(N-1):
            if (i >> j) & 1:
                temp_list.append(j+1)
                k=j+1

        temp_list = temp_list[::-1]
        
        for x in temp_list:
            temp_arr[x-1],temp_arr[k]=temp_arr[k],temp_arr[x-1]
            current_cost = current_cost + (k - (x-1) +1)
            k=k-1

        if current_cost == C:
            return " ".join(map(str, temp_arr))
        
    return "IMPOSSIBLE"


T = int(input())
for i in range(1, T + 1):
    result = solve()
    print(f"Case #{i}: {result}")