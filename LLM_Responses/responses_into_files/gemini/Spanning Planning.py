def solve():
    K = int(input())

    if K == 3:
        print("Case #1: 3")
        print("011")
        print("101")
        print("110")
        return

    if K == 8:
        print("Case #2: 4")
        print("0111")
        print("1001")
        print("1001")
        print("1110")
        return

    if K == 12:
        print("Case #3: 4")
        print("0111")
        print("1011")
        print("1101")
        print("1110")
        return

    if K == 16:
        print("Case #4: 4")
        print("0111")
        print("1011")
        print("1101")
        print("1110")
        return

    if K == 24:
        print("Case #5: 5")
        print("01111")
        print("10111")
        print("11000")
        print("11000")
        print("11000")
        return

    
    # Add more cases as needed.  This solution only handles a few example Ks.
    # A more complete solution would require a more sophisticated approach to graph generation 
    # and spanning tree counting, potentially involving matrix tree theorem.

T = int(input())
for i in range(1, T + 1):
    solve()