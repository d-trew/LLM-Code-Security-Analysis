def find_missing_set(T, F):
    for _ in range(T):
        input()  # Read the line containing N and the missing set
        sets = list(input().strip())
        
        for _ in range(F + 1):
            pos = int(input()) - 1
            print(pos // 5)  # Send the index of the missing set
        
        input()  # Read the line containing the order of the remaining sets

# Example usage:
T, F = map(int, input().split())
find_missing_set(T, F)