T, N, K = map(int, input().split())

for t in range(T):
    arr = list(map(int, input().split()))
    
    bumps_left = K
    while True:
        sorted_arr = True
        for i in range(N):
            if arr[i] != i + 1:
                sorted_arr = False
                break
        if sorted_arr:
            break

        colors = {}
        color_count = 0
        new_arr = [0] * N
        
        for i in range(N):
            if arr[i] not in colors:
                colors[arr[i]] = color_count
                color_count +=1
            
        color_arrays = [[] for _ in range(color_count)]
        for i in range(N):
            color_arrays[colors[arr[i]]].append(i)

        
        for i in range(color_count):
          import random
          random.shuffle(color_arrays[i])

        idx = 0
        for i in range(color_count):
          for j in color_arrays[i]:
            new_arr[j] = arr[j]

        
        print(*[x+1 for x in new_arr])
        arr = list(map(int, input().split()))
        bumps_left -=1
        if bumps_left == 0 :
          break