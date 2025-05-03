def decode_phone_number(s):
    digit_map = {
        'ZERO': '0', 'ONE': '1', 'TWO': '2', 'THREE': '3', 'FOUR': '4',
        'FIVE': '5', 'SIX': '6', 'SEVEN': '7', 'EIGHT': '8', 'NINE': '9'
    }
    count = [0] * 10
    for char in s:
        for word, digit in digit_map.items():
            if word.startswith(char):
                count[int(digit)] += 1
    
    result = []
    for i in range(10):
        result.extend([str(i)] * count[i])
    
    return ''.join(result)

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    T = int(data[0])
    results = []
    index = 1
    for _ in range(T):
        s = data[index]
        result = decode_phone_number(s)
        results.append(f"Case #{_ + 1}: {result}")
        index += 1
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()