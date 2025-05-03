# Write a Python program based on this description.
# Return ONLY the Python code with no additional explanation or formatting.

import sys

def solve(towers):
    # Check if all towers are valid megatowers
    for tower in towers:
        if not is_valid_megatower(tower):
            return "IMPOSSIBLE"

    # Combine all towers into a single megatower
    megatower = []
    for tower in towers:
        megatower.extend(tower)

    # Check if the megatower is valid
    if not is_valid_megatower(megatower):
        return "IMPOSSIBLE"

    # Return the megatower as a string
    return "".join(megatower)

def is_valid_megatower(tower):
    # Check if all letters of the alphabet are present in the tower
    for letter in range(ord('A'), ord('Z') + 1):
        if not any(block == chr(letter) for block in tower):
            return False

    # Check if there are no non-contiguous groups of letters
    last_letter = None
    current_group = []
    for letter in tower:
        if last_letter is None or last_letter == letter:
            current_group.append(letter)
        else:
            if len(current_group) > 1:
                return False
            current_group = [letter]
        last_letter = letter

    # Check if the tower ends with a non-contiguous group of letters
    if len(current_group) > 1:
        return False

    return True

# Read input
t = int(input())
for case in range(1, t + 1):
    n = int(input())
    towers = []
    for _ in range(n):
        tower = list(input().upper())[::-1]
        towers.append(tower)
    print("Case #{}".format(case), solve(towers))