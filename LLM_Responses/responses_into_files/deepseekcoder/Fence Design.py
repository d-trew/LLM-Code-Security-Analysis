import sys
from typing import List, Tuple

def solve(poles: List[Tuple[int, int]], fence1: Tuple[int, int], fence2: Tuple[int, int]) -> List[Tuple[int, int]]:
    # Check if the poles are collinear
    (x1, y1), (x2, y2), (x3, y3) = sorted(poles)[1:]
    if (y2 - y1) * (x3 - x2) == (y3 - y2) * (x2 - x1):
        return []
    
    # Sort the poles by their X-coordinates
    poles.sort()
    
    # Initialize a list to keep track of the fences
    fences = [fence1, fence2]
    
    # Iterate over all the remaining poles and add new fences where necessary
    for i in range(len(poles)):
        if not is_valid_fence((poles[i-1], poles[i]), fences):
            fences.append((i, i+1))
    
    return fences[2:]  # Return the new fences (not including the existing ones)

def is_valid_fence(fence: Tuple[int, int], fences: List[Tuple[int, int]]) -> bool:
    # Check if any of the existing fences intersect with the new fence
    for old_fence in fences:
        if (fence[0] in old_fence and fence[1] not in old_fence) or \
           (fence[1] in old_fence and fence[0] not in old_fence):
            return False
    return True

def main():
    T = int(sys.stdin.readline().strip())
    for t in range(T):
        N = int(sys.stdin.readline().strip())
        poles = [tuple(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
        fence1 = tuple(map(lambda x: int(x) + 1, sys.stdin.readline().strip().split()))
        fence2 = tuple(map(lambda x: int(x) + 1, sys.stdin.readline().strip().split()))
        
        fences = solve(poles, fence1, fence2)
        
        print("Case #{}: {}".format(t+1, len(fences)))
        for f in fences:
            print(*f)

if __name__ == "__main__":
    main()