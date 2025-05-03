import itertools

T = int(input())

for i in range(1, T + 1):
    B, M = map(int, input().split())
    
    def is_possible(B, M):
        if M == 0 or M > (2 ** (B - 1) - 1):
            return False
        
        # Generate all possible ways to build slides using itertools.product
        for way in itertools.product([0, 1], repeat=B-1):
            if sum(way[:M]) == M:
                print("Case #{}: POSSIBLE".format(i))
                # Print the matrix representation of the slides
                for j in range(len(way) + 1):
                    line = " ".join([str(x) for x in way[:j]]) + " 0" * (B - j)
                    print(line)
                break
        else:
            print("Case #{}: IMPOSSIBLE".format(i))
    
    is_possible(B, M)