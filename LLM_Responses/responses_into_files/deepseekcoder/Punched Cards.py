def print_punched_card(r, c):
    # Initialize an empty list to store the ASCII art of the punched card
    punched_card = []
    
    for i in range(2 * r + 1):
        if i % 2 == 0:
            # Even rows are filled with "." and "-" characters
            row = ["+"] + ["-"] * c + ["+"]
            punched_card.append("".join(row))
        else:
            # Odd rows are filled with "|" character followed by "." and "|" characters
            row = ["|"] + ["."] * c + ["|"]
            punched_card.append("".join(row))
    
    return "\n".join(punched_card)

# Read the number of test cases
t = int(input())
for i in range(1, t + 1):
    # Read the size of the punched card
    r, c = map(int, input().split())
    
    # Print the ASCII art of the punched card
    print("Case #{}:\n{}".format(i, print_punched<｜begin▁of▁sentence｜>_card(r, c)))