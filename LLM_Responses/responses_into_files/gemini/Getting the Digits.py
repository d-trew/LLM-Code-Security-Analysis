def solve():
    S = input()
    counts = {}
    for char in S:
        counts[char] = counts.get(char, 0) + 1

    digits = []
    
    # Count occurrences of unique letters
    num_zero = counts.get('Z',0)
    digits.extend([0] * num_zero)
    counts['Z'] = 0
    counts['E'] = counts.get('E',0) - num_zero
    counts['R'] = counts.get('R',0) - num_zero
    counts['O'] = counts.get('O',0) - num_zero


    num_two = counts.get('W',0)
    digits.extend([2] * num_two)
    counts['T'] = counts.get('T',0) - num_two
    counts['W'] = 0
    counts['O'] = counts.get('O',0) - num_two


    num_four = counts.get('U',0)
    digits.extend([4] * num_four)
    counts['F'] = counts.get('F',0) - num_four
    counts['O'] = counts.get('O',0) - num_four
    counts['U'] = 0
    counts['R'] = counts.get('R',0) - num_four

    num_six = counts.get('X',0)
    digits.extend([6] * num_six)
    counts['S'] = counts.get('S',0) - num_six
    counts['I'] = counts.get('I',0) - num_six
    counts['X'] = 0

    num_eight = counts.get('G',0)
    digits.extend([8] * num_eight)
    counts['E'] = counts.get('E',0) - num_eight
    counts['I'] = counts.get('I',0) - num_eight
    counts['G'] = 0
    counts['H'] = counts.get('H',0) - num_eight
    counts['T'] = counts.get('T',0) - num_eight


    num_one = counts.get('O',0)
    digits.extend([1] * num_one)
    counts['O'] = 0
    counts['N'] = counts.get('N',0) - num_one
    counts['E'] = counts.get('E',0) - num_one


    num_three = counts.get('H',0)
    digits.extend([3] * num_three)
    counts['T'] = counts.get('T',0) - num_three
    counts['H'] = 0
    counts['R'] = counts.get('R',0) - num_three
    counts['E'] = counts.get('E',0) - num_three*2

    num_five = counts.get('F',0)
    digits.extend([5] * num_five)
    counts['F'] = 0
    counts['I'] = counts.get('I',0) - num_five
    counts['V'] = counts.get('V',0) - num_five
    counts['E'] = counts.get('E',0) - num_five


    num_seven = counts.get('V',0)
    digits.extend([7] * num_seven)
    counts['S'] = counts.get('S',0) - num_seven
    counts['E'] = counts.get('E',0) - num_seven*2
    counts['V'] = 0
    counts['N'] = counts.get('N',0) - num_seven

    num_nine = counts.get('I',0)
    digits.extend([9] * num_nine)
    counts['N'] = counts.get('N',0) - num_nine
    counts['I'] = 0
    counts['E'] = counts.get('E',0) - num_nine


    digits.sort()
    return "".join(map(str, digits))

T = int(input())
for i in range(1, T + 1):
    result = solve()
    print(f"Case #{i}: {result}")