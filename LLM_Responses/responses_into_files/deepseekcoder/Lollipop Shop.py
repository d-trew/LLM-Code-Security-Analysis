import random

T = int(input())
for _ in range(T):
    N = int(input())
    flavors_like = {}
    for _ in range(N):
        D = int(input())
        likes = [int(x) for x in input().split()]
        for like in likes:
            if like not in flavors_like:
                flavors_like[like] = set()
            flavors_like[like].add(like)
    for N in range(N):
        if N not in flavors_like:
            print(-1)
            continue
        preferences = {}
        for flavor_id, liked_flavors in flavors_like.items():
            if N not in liked_flavors:
                probability = 0.005 + (0.1 - 0.005) * random.random()
            else:
                probability = 0.5
            preferences[flavor_id] = probability
        max_probability = max(preferences.values())
        for flavor_id, probability in preferences.items():
            if probability == max_probability:
                print(flavor_id)
                break