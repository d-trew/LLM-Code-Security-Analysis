import sys

def solve(input_string):
    # Replace the digits of the phone number with their corresponding uppercase English representation
    phone_number = input_string.replace("ZERO", "0").replace("ONE", "1").replace("TWO", "2").replace("THREE", "3").replace("FOUR", "4").replace("FIVE", "5").replace("SIX", "6").replace("SEVEN", "7").replace("EIGHT", "8").replace("NINE", "9")
    # Sort the phone number in nondecreasing order
    sorted_phone_number = "".join(sorted(phone_number))
    return sorted_phone_number

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        input_string = sys.stdin.readline().strip()
        result = solve(input_string)
        print("Case #" + str(i+1) + ": " + result)