import math

def number_of_operations(S, E):
    count = 0
    while S != E:
        if S[0] == '1':
            S = '0' + S[1:]
            count += 1
        else:
            S = '1' + S
            count += 1
    return count

if __name__ == "__main__":
    T = int(input())
    for i in range(T):
        S, E = input().split()
        print("Case #" + str(i+1) + ":", number_of_operations(S, E))