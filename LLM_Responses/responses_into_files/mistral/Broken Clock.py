import math
def clock_angle_to_time(hours_hand_angle, minutes_hand_angle, seconds_hand_angle):
    hours_hand_rotation = (hours_hand_angle / 360) * 12
    minutes_hand_rotation = (minutes_hand_angle / 360) * 60
    seconds_hand_rotation = (seconds_hand_angle / 360) * 6

    total_minutes = math.floor(hours_hand_rotation * 60 + minutes_hand_rotation)
    remaining_seconds = int((total_minutes + seconds_hand_rotation) % 60)

    hours = math.floor(total_minutes / 60)
    nanoseconds = (hours_hand_rotation * 10**9 + minutes_hand_rotation * 10**8 + seconds_hand_rotation * 10**7) % 10**9

    return f"Case #1: {hours} {remaining_seconds} {nanoseconds}"

T = int(input())
for _ in range(T):
    hours_hand_angle, minutes_hand_angle, seconds_hand_angle = map(int, input().split())
    print(clock_angle_to_time(hours_hand_angle, minutes_hand_angle, seconds_hand_angle))