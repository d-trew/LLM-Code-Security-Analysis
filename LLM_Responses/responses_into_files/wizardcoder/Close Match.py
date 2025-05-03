import sys

def find_minimum(s):
    def fill_digits(score, missing_count):
        if len(score) == 1 or missing_count == 0:
            return score
        for i in range(len(score)):
            if score[i] == '?':
                for j in range(10):
                    new_score = score[:i] + str(j) + score[i+1:]
                    yield from fill_digits(new_score, missing_count - 1)

    def get_minimum(scores):
        coder, jammer = scores
        min_diff = abs(int(coder) - int(jammer))
        for i in range(len(coder)):
            if coder[i] == '?' and jammer[i] != '?':
                for digit in fill_digits(coder[:i] + '0' + coder[i+1:], missing_count):
                    diff = abs(int(digit) - int(jammer))
                    if diff < min_diff or (diff == min_diff and int(digit) > int(coder)):
                        min_diff, coder = diff, digit + jammer[i+1:]
            elif coder[i] != '?' and jammer[i] == '?':
                for digit in fill_digits(coder[:i] + str(jammer[i]) + coder[i+1:], missing_count):
                    diff = abs(int(digit) - int(coder))
                    if diff < min_diff or (diff == min_diff and int(digit) < int(coder)):
                        min_diff, jammer = diff, coder[:i+1] + digit[i] + jammer[i+1:]
        return coder, jammer
    missing_count = s.count('?')
    if missing_count == 0:
        return s, s
    return get_minimum(get_minimum([''.join(sorted(s[:len(s)//2])[::-1], ''.join(sorted(s[len(s)//2:])[::-1])])) if missing_count % 2 == 0 else s.replace('?', '9'))

T = int(input())
for i in range(1, T+1):
    coder, jammer = input().split()
    coder_filled, jammer_filled = find_minimum(coder), find_minimum(jammer)
    print(f"Case #{i}: {coder_filled} {jammer_filled}")