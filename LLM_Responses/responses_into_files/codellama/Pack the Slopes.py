import sys
input = sys.stdin.readline
T=int(input())
for i in range(1,T+1):
    N=int(input())
    slope_list=[[] for _ in range(N)]
    for j in range(N-1):
        Ui,Vi,Si,Ci=map(int,input().split())
        if Ui not in slope_list[Ui-1]:
            slope_list[Ui-1].append([Vi,Si,Ci])
    max_skier=0
    min_expense=0
    for k in range(N):
        skier=1
        expense=0
        while skier<=max_skier:
            if k not in slope_list[k]:
                break
            for l in range(len(slope_list[k])):
                if slope_list[k][l][0]==k+1 and slope_list[k][l][2]>skier:
                    skier+=1
                    expense+=slope_list[k][l][3]*skier
        max_skier=max(max_skier,skier)
        min_expense=min(min_expense,expense)
    print("Case #"+str(i)+": "+str(max_skier)+" "+str(min_expense))