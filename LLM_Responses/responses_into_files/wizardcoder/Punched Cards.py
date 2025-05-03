import sys

def draw_punched_card(R,C):
    for i in range(1,R+1):
        if i==1:
            print("."*(2*C-1) + "+")
        else:
            print(".|" + "."*(C-2) + "+")
        
        for j in range(1,C):
            if j<C:
                print(".-+" + "-"*(C-2), end="+")
    print()
    
T = int(input())
for i in range(1,T+1):
    R, C = map(int, input().split())
    print("Case #%d:" %i)
    draw_punched_card(R-2,C-2)<|im_sep|>