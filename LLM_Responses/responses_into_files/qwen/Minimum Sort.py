import sys

def query_min(i, j):
    print(f"Q {i} {j}")
    sys.stdout.flush()
    response = input().strip()
    if not response.isdigit():
        return -1
    return int(response)

def swap(i, j):
    print(f"S {i} {j}")
    sys.stdout.flush()

def sort_list(N):
    for i in range(N-1):
        min_pos = i
        for j in range(i+1, N):
            pos = query_min(i, j)
            if pos == -1:
                return -1
            if pos < min_pos:
                min_pos = pos
        if min_pos != i:
            swap(min_pos, i)

def main():
    T, N = map(int, input().strip().split())
    for _ in range(T):
        if sort_list(N) == -1:
            return -1

if __name__ == "__main__":
    main()