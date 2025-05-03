def balanced_string(s):
    count = [0]*len(s)
    stack = []
    result = ['']*len(s)
    
    for i, c in enumerate(s):
        if c == '(':
            stack.append(i)
        else:
            j = stack.pop()
            count[j] += 1
            count[i] += 1
            
    for i, c in enumerate(count):
        result[i] = str(c) if s[i] == '(' else ''
        
    return ''.join(result).replace('0', '')

t = int(input())
for case_no in range(1, t + 1):
    s = input()
    print("Case #{}: {}".format(case_no, balanced_string(s)))