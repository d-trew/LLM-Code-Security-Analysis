def find_winning_program(adversaries):
    def beats(move1, move2):
        return (move1 == 'R' and move2 == 'S') or \
               (move1 == 'P' and move2 == 'R') or \
               (move1 == 'S' and move2 == 'P')

    for length in range(1, 501):
        for program in (''.join(p) for p in itertools.product('RPS', repeat=length)):
            if all(beats(program[i % len(program)], adv[i % len(adv)]) for i, adv in enumerate(adversaries)):
                return program
    return "IMPOSSIBLE"

import itertools

T = int(input())
for t in range(T):
    A = int(input())
    adversaries = [input().strip() for _ in range(A)]
    result = find_winning_program(adversaries)
    print(f"Case #{t+1}: {result}")