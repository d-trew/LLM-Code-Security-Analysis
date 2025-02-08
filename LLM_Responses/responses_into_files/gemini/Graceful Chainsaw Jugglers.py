def max_jugglers(R, B):
    if R == 0 or B == 0:
        return 1
    
    count = 0
    k = 0
    while True:
        k += 1
        required_red = k * (k + 1) // 2
        required_blue = k * (k + 1) // 2
        if required_red > R or required_blue > B:
            k -= 1
            break

    
    ans = k

    
    for i in range(k + 1):
        red_left = R - i * (i+1) //2
        blue_left = B - i * (i+1) //2

        if red_left < 0 or blue_left < 0:
            continue
        
        ans = max(ans, i + min(red_left, blue_left) + (max(red_left,blue_left) - min(red_left,blue_left)) //(i+1) + (max(red_left, blue_left) - min(red_left, blue_left)) % (i+1) )

    return ans


T = int(input())
for x in range(1, T + 1):
    R, B = map(int, input().split())
    y = max_jugglers(R, B)
    print(f'Case #{x}: {y}')