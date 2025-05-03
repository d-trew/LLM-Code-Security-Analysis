import random
t, n, k = map(int, input().split())
for _ in range(t):
    balls = list(map(int, input().split()))
    boxes = [i for i in range(1, n+1)]
    color_box = {}
    for i in range(k):
        for j in range(n):
            if random.random() < 0.5:
                temp = boxes[boxes.index(balls[j])]
                balls[j] = balls[balls.index(temp)]
                boxes.remove(temp)
        for j in range(len(boxes)):
            color_box.setdefault((j+1)%3, []).append(boxes[j])
    print(*balls)