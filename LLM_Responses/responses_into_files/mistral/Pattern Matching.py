import re

T = int(input())

for _ in range(T):
    N = int(input())
    patterns = [input() for _ in range(N)]

    min_length = min(len(pattern) for pattern in patterns)
    max_length = 104

    for length in range(min_length, max_length + 1):
        name = ''
        for i in range(length):
            for pattern in patterns:
                if i < len(pattern) and pattern[i] == '*':
                    name += chr(65 + (i % 26))
                else:
                    name += pattern[i]
            break

        if all(re.sub('[^A-Z*]', '', pattern) == re.sub('[^A-Z*]', '', name) for pattern in patterns):
            print(f'Case #{_+1}: {name}')
            break
    else:
        print(f'Case #{_+1}: *')