def main():
    T = int(input())
    for i in range(1, T + 1):
        N = int(input())
        patterns = []
        for j in range(N):
            patterns.append(input().strip())
        name = ''
        found_name = False
        for c in ascii_uppercase:
            if not found_name:
                for pattern in patterns:
                    if '*' in pattern:
                        index = pattern.index('*')
                        if len(pattern) == 1 or (len(pattern[0:index]) != '' and name[:index] == pattern[0:index] and name[-1] not in ascii_uppercase):
                            found_name = True
                            break
                    else:
                        if len(name) < len(pattern):
                            for c in ascii_uppercase:
                                name += c
                                if pattern == name:
                                    found_name = True
                                    break
                                elif '*' not in pattern and pattern != name:
                                    name = ''
        print(f"Case #{i}: {name}")

if __name__ == "__main__":
    main()