def solve(s):
    zero_to_nine = ['ZERO', 'ONE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE']
    for i in range(len(zero_to_nine)):
        s = s.replace(zero_to_nine[i], str(i))
    return ''.join(sorted(s))

for t in range(int(input())):
    print('Case #{}: {}'.format(t+1, solve(input())))