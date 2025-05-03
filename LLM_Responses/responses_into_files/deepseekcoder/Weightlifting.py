Here is the Python code for this problem:


from collections import deque

def solve():
    T = int(input().strip())
    for t in range(1, T + 1):
        E, W = map(int, input().split())
        exercises = [list(map(int, input().split())) for _ in range(E)]
        
        operations = 0
        stack = deque()
        for exercise in exercises:
            while True:
                if not stack or (stack[-1] != max(exercise) and len(stack) < W):
                    stack.append(max(exercise))
                    operations += 1
                elif stack[-1] == max(exercise):
                    stack.pop()
                    operations += 1
                if all(weight in stack for weight in exercise):
                    break
        
        print("Case #{}: {}".format(t, operations))

solve()

This code uses a deque (double-ended queue) as the machine's stack. For each exercise, it adds weights to the top of the stack until all weights are present in the stack or until the stack is full. It then removes the largest weight from the stack and repeats this process for the next exercise. The number of operations required is tracked by incrementing a counter each time an operation is performed.