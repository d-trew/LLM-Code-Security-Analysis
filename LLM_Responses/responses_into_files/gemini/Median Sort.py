T, N, Q = map(int, input().split())

def solve():
    elements = list(range(1, N + 1))
    queries_left = Q // T

    known_medians = {}

    def ask_median(i, j, k):
        print(i, j, k)
        return int(input())

    def find_sorted_order(elements):
        
        if len(elements) <=2:
            return elements

        #Simplified approach for demonstration purposes.  A more efficient algorithm would be needed for larger N.

        sorted_elements = []
        unplaced = elements.copy()

        # Find potential min and max (very naive initial guess)
        min_candidate = unplaced[0]
        max_candidate = unplaced[0]
        for i in range(1,len(unplaced)):
            median = ask_median(min_candidate,max_candidate,unplaced[i])
            if median == min_candidate:
                max_candidate = unplaced[i]
            elif median == max_candidate:
                min_candidate = unplaced[i]
            else:
                min_candidate = min(min_candidate,unplaced[i])
                max_candidate = max(max_candidate,unplaced[i])

        sorted_elements.append(min_candidate)
        sorted_elements.append(max_candidate)
        unplaced.remove(min_candidate)
        unplaced.remove(max_candidate)

        # Add remaining elements (again, very naive approach)
        sorted_elements.extend(unplaced)

        return sorted_elements

    sorted_order = find_sorted_order(elements)
    print(*sorted_order)
    result = int(input())
    if result == -1:
        exit()


for _ in range(T):
    solve()