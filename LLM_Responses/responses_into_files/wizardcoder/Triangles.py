def main():
    T = int(input())
    for t in range(1, T+1):
        N = int(input())
        points = []
        for i in range(N):
            x, y = map(int, input().split())
            points.append((x,y))
        
        # Your code here to find the maximum set of triangles and print it
        max_triangles = []
        print("Case #{}: {}".format(t), end="\n")
        for triangle in max_triangles:
            print(triangle[0], triangle[1], triangle[2])
            
main()