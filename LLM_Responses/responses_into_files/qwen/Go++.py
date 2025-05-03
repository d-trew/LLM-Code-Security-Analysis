def generate_programs(N, L, G, B):
    if B in G:
        return "IMPOSSIBLE"
    
    def can_produce(s, target):
        stack = []
        for char in s:
            if char == '1':
                stack.append('0')
            else:
                if not stack or stack[-1] != '0':
                    return False
                stack.pop()
        return ''.join(stack) == target
    
    def find_programs(target, length):
        if length == 0:
            return []
        if length == 1:
            return ['0'] if can_produce('0', target) else ['1']
        
        programs = []
        for i in range(length):
            prefix = '0' * i + '1' * (length - i)
            suffixes = find_programs(target[len(prefix):], length - len(prefix))
            for suffix in suffixes:
                if can_produce(prefix, target[:len(prefix)]) and can_produce(suffix, target[len(prefix):]):
                    programs.append(prefix + suffix)
        return programs
    
    good_programs = []
    bad_programs = []
    
    for s in G:
        good_programs.extend(find_programs(s, L))
    
    for i in range(1 << L):
        binary_str = format(i, '0' + str(L) + 'b')
        if can_produce(binary_str, B):
            continue
        bad_programs.append(binary_str)
    
    return " ".join(good_programs[:L//2]) + " " + " ".join(bad_programs[:L//2])

# Read input
T = int(input())
results = []
for i in range(1, T + 1):
    N, L = map(int, input().split())
    G = [input().strip() for _ in range(N)]
    B = input().strip()
    results.append(f"Case #{i}: {generate_programs(N, L, G, B)}")

# Print all results
for result in results:
    print(result)