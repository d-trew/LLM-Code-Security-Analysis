import sys
def solve(N,P):
    if N==2:
        return 'AB'
    else:
        ans=''
        for i in range(len(P)):
            if P[i]%2!=0:
                ans+=chr(ord('A')+i)
        for i in range(len(P)):
            if P[i]>1:
                ans+=chr(ord('A')+i)*int((P[i]-1)/2)
        return ans
T=int(input())
for t in range(T):
    N,P=[int(x) for x in input().split()]
    print("Case #"+str(t+1)+": "+solve(N,P))