def main():
    T = int(input())
    for i in range(1, T + 1):
        E, W = map(int, input().split())
        X = [list(map(int, input().split())) for _ in range(E)]
        
        min_ops = 0
        stack = []
        
        for x in X:
            for j in range(W):
                if not stack or stack[-1] != j + 1:
                    min_ops += 1
                    stack.append(j + 1)
                elif len(stack) > 0 and stack[-1] == j + 1:
                    stack.pop()
                    
        print("Case #" + str(i) + ": " + str(min_ops))

main()