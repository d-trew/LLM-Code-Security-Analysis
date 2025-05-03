def main():
    T = int(input()) # read number of test cases
    for i in range(T):
        V, P = map(int, input().split()) # read V and P on turn 100
        if P == 100:
            print("100 99") # insert your token into vase 99
        else:
            pass # do nothing
            
main()