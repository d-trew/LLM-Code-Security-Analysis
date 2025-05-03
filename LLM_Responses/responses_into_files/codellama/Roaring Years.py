import sys

def is_roaring_year(year):
    # Check if the year is a concatenation of two or more distinct consecutive positive integers in increasing order
    str_year = str(year)
    for i in range(len(str_year)-1):
        if str_year[i] == '0':
            continue
        if int(str_year[i]) + 1 != int(str_year[i+1]):
            return False
    return True

if __name__ == "__main__":
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    # Get the number of test cases
    T = data[0]
    for i in range(1, T+1):
        year = data[i]
        if is_roaring_year(year):
            print("Case #{}: {}".format(i, year))
        else:
            next_year = year + 1
            while not is_roaring_year(next_year):
                next_year += 1
            print("Case #{}: {}".format(i, next_year))