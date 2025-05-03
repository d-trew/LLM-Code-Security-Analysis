def find_last_number(N):
    if N == 0:
        return "INSOMNIA"
    
    seen_digits = set()
    i = 1
    while len(seen_digits) < 10:
        current_number = i * N
        for digit in str(current_number):
            seen_digits.add(int(digit))
        i += 1
    
    return current_number

def main():
    T = int(input())
    results = []
    for case_num in range(1, T + 1):
        N = int(input())
        result = find_last_number(N)
        results.append(f"Case #{case_num}: {result}")
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()