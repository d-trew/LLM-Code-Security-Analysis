def main():
    T = int(input())  # number of test cases
    
    for i in range(T):
        B, S, N = map(int, input().split())  # number of buildings and slides, and operations to perform
        
        slides = [[False] * (S + 1) for _ in range(B + 1)]  # initialize all slides as disabled
        
        for j in range(N):
            X, Y = map(int, input().split())  # read slide x and y values
            if X < Y:  # enable the slide from building X to building Y
                for k in range(X * S // X, (Y * S + 1) // Y + 1, S):  # iterate over all multiples of M between L and R
                    slides[X][k] = True
            else:  # disable the slide from building X to building Y
                for k in range(X * S // X, (Y * S + 1) // Y + 1, S):
                    slides[X][k] = False
        
        fun_slides = []
        for j in range(S):
            count = sum([slides[b][j] for b in range(B + 1)])  # count the number of enabled slides from building j
            if count == B - 1:  # j is a circuit start
                fun_slides.append(j * S // (B - 1))  # enable this slide to make the state fun
        
        print("Case #{}: {}".format(i + 1, " ".join([str(x) if x else "X" for x in fun_slides]))  # output the result
    
    return 0

if __name__ == "__main__":
    main()