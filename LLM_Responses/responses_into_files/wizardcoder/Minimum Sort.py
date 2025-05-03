def main():
    T = int(input())
    N = int(input())
    for t in range(T):
        exchange_count = 0
        swaps = []
        min_range = {}
        
        def get_minimum_in_range(i, j):
            nonlocal exchange_count
            nonlocal min_range
            
            if i > j:
                return -1
            
            if (i, j) in min_range:
                return min_range[(i, j)]
            
            exchange_count += 1
            print(f"D {i} {j}", flush=True)
            response = int(input())
            if response == -1:
                exit()
            
            if response < i or response > j:
                return get_minimum_in_range(i, j)
            
            min_range[(i, j)] = response
            return response
        
        def swap(i, j):
            nonlocal exchange_count
            print(f"S {i} {j}", flush=True)
            input()
            exchange_count += 1
            
        def sort():
            for i in range(N-1):
                min_pos = get_minimum_in_range(i, N-1)
                
                if min_pos == -1:
                    exit()
                
                if i < min_pos:
                    swap(i, min_pos)
        
        sort()
        print("DONE")
        input()
        
main()