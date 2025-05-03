for tc in range(int(input())):
    n = int(input())
    rc_list = []
    for i in range(n):
        ri, ci = map(int, input().split())
        rc_list.append([ri, ci])
    min_turns = 0
    for i in range(n-1):
        if rc_list[i][0] != rc_list[-1][0] or rc_list[i][1] != rc_list[-1][1]:
            min_turns += 1
    print("Case #" + str(tc+1) + ": " + str(min_turns))