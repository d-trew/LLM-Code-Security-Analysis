import math
def solve(N):
    return "IMPOSSIBLE" if N%2==0 else "POSSIBLE"
for t in range(int(input())):
    n=int(input())
    x=[list(map(int,input().split())) for _ in range(n+1)]
    y=[list(map(int,input().split())) for _ in range(n+1)]
    z=[list(map(int,input().split())) for _ in range(n+1)]
    ans=solve(n)
    if ans=="POSSIBLE":
        print("Case #"+str(t+1)+": "+ans)
        for i in range(1,n+1):
            min_dist=float('inf')
            closest_sweet=0
            for j in range(1,n+1):
                dist=math.sqrt((x[i][0]-z[j][0])**2+(y[i][1]-z[j][1])**2)
                if dist<min_dist:
                    min_dist=dist
                    closest_sweet=j
            print(str(i)+" "+str(closest_sweet))