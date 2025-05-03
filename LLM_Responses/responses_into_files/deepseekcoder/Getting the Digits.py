def decode_phone_number(s):
    mapping = {'ZERO': '0', 'ONE': '1', 'TWO': '2', 'THREE': '3', 'FOUR': '4',
               'FIVE': '5', 'SIX': '6', 'SEVEN': '7', 'EIGHT': '8', 'NINE': '9'}
    count_mapping = {'ZERO': 0, 'ONE': 0, 'TWO': 0, 'THREE': 0, 'FOUR': 0,
                     'FIVE': 0, 'SIX': 0, 'SEVEN': 0, 'EIGHT': 0, 'NINE': 0}
    for word in ['ZERO', 'ONE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE']:
        while word in s:
            count_mapping[word] += 1
            s = s.replace(word, '', 1)
    return ''.join([count_mapping[key] * mapping[key] for key in count_mapping])

t = int(input().strip())
for i in range(t):
    s = input().strip()
    print('Case #{}: {}'.format(i + 1, decode_phone_number(s)))