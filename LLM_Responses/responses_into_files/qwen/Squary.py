def find_squary_elements(N, K, E):
    sum_E = sum(E)
    sum_E_square = sum(x**2 for x in E)
    target = (sum_E + K)**2 - sum_E_square

    if target == 0:
        return "IMPOSSIBLE"
    
    added_elements = []
    for _ in range(K):
        if target % (K - len(added_elements)) == 0:
            added_element = target // (K - len(added_elements))
            added_elements.append(added_element)
            sum_E += added_element
            sum_E_square += added_element**2
            target = (sum_E + K)**2 - sum_E_square
    
    if sum_E_square != (sum_E + K)**2:
        return "IMPOSSIBLE"
    
    return ' '.join(map(str, added_elements))

T = int(input())
results = []
for i in range(1, T+1):
    N, K = map(int, input().split())
    E = list(map(int, input().split()))
    results.append(f"Case #{i}: {find_squary_elements(N, K, E)}")

for result in results:
    print(result)