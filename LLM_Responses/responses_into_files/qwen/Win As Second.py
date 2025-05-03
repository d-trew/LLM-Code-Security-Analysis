import sys

def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        print(N - 1)
        for i in range(1, N):
            print(f"{i} {i + 1}")
        
        M = int(input())
        for _ in range(M):
            K = int(input())
            vertices = list(map(int, input().split()))
            if len(vertices) != K or any(v < 1 or v > N for v in vertices):
                sys.stdout.write("-1\n")
                return
            # Vreni's turn: color the last vertex and its neighbors red
            last_vertex = vertices[-1]
            neighbors = [v for v in range(1, N + 1) if v != last_vertex and (v < last_vertex and v % last_vertex == 0 or v > last_vertex and v // last_vertex == last_vertex)]
            num_neighbors = len(neighbors)
            if K - 1 != num_neighbors:
                sys.stdout.write("-1\n")
                return
            for neighbor in neighbors:
                print(f"{neighbor} {neighbor + 1}")

if __name__ == "__main__":
    main()