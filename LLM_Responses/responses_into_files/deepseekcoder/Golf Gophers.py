import random
from collections import defaultdict

def simulate_gopher(windmills):
    gopher = random.choice(list(windmills.keys()))
    windmill = windmills[gopher]
    del windmills[gopher]
    if len(windmill) == 1:  # If the windmill has only one blade, remove it from the dictionary
        del windmills[len(windmill)-1]
    else:
        new_blade = (windmill[-2], )
        windmills[gopher] = new_blade
    return len(windmills)+1 if windmills else 0

def gophers_in_course(T, N, M):
    for _ in range(T):
        windmills = defaultdict(tuple)
        for i in range(N-1, -1, -1):
            blades = random.randint(2, 18)
            windmills[i] = tuple(range(blades))
        while True:
            gophers = simulate_gopher(windmills)
            if not (0 <= gophers <= M):
                print('Wrong Answer')
                return
            elif len(windmills) == 0:
                print(f'Accepted: {gophers}')
                break