import sys
def main():
    T = int(input())
    for i in range(1, T + 1):
        C = int(input())
        B = list(map(int, input().split()))
        if sum(B) > C:
            print("Case #{}: IMPOSSIBLE".format(i))
        else:
            ramp_count = 0
            for b in B:
                if b == 1 and ramp_count % 2 != 0:
                    ramp_count += 1
                elif b > 0:
                    print("Case #{}: IMPOSSIBLE".format(i))
                    break
            else:
                rows = (ramp_count + sum(B) - 1) // 2
                layout = ['.' * C] * rows
                for j in range(ramp_count):
                    layout[j] = '\\' + '/' * (C - 2) + '.'
                print("Case #{}: {}".format(i))
                for row in layout:
                    print(row)
main()