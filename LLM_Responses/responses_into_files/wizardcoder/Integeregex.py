def main():
    T = int(input())
    for i in range(T):
        A, B = map(int, input().split())
        R = input()
        
        count = 0
        for num in range(A, B+1):
            if match_regex(R, str(num)):
                count += 1
                
        print("Case #{}: {}".format(i+1, count))
    
def match_regex(R, D):
    if R == "":
        return False
    i = 0
    j = 0
    while i < len(D) and j < len(R):
        if D[i] == '(':
            break
        elif R[j] == '.':
            i += 1
        elif R[j] == '*':
            return match_regex(R[:j-1], D[i+1:]) or match_regex(R, D[i+1:])
        else:
            if D[i] != R[j]:
                return False
            i += 1
            j += 1
    return i == len(D) and j == len(R)
    
if __name__ == "__main__":
    main()