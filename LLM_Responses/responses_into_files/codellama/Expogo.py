import sys
input = sys.stdin.readline()
t=int(input)
for i in range(1,t+1):
    x,y=map(int,input.split())
    if x==0 and y==0:
        print("Case #"+str(i)+": IMPOSSIBLE")
    elif x>0 and y>0:
        print("Case #"+str(i)+": NNNEEEESSSSSSTTTT")
    elif x<0 and y<0:
        print("Case #"+str(i)+": WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW