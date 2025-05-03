import math

def pyramidification_cost(S, P):
    # Calculate the sum of the pyramidification costs over all valid choices of L and R
    sum = 0
    for L in range(min(S - 3, S // 2)):
        for R in range(min(S - 3, (S + 1) // 2)):
            # Calculate the remaining stacks after removing the leftmost and rightmost stacks
            remaining_stacks = P[L:S - R]
            # Check if the remaining stacks have the pyramid property
            has_pyramid_property = True
            for i in range(len(remaining_stacks) - 1):
                if remaining_stacks[i] <= remaining_stacks[i + 1]:
                    has_pyramid_property = False
                    break
            if has_pyramid_property:
                # Calculate the pyramidification cost of the remaining stacks
                pyramidification_cost = sum(remaining_stacks) % (109 + 7)
                sum += pyramidification_cost
    return sum % (109 + 7)

# Test cases
def test_pyramidification_cost():
    S = 3000
    P = [1, 6, 2, 5, 7]
    assert pyramidification_cost(S, P) == 16
    S = 500
    P = [1, 6, 2, 5, 7]
    assert pyramidification_cost(S, P) == 3
    S = 106
    P = [1, 6, 2, 5, 7]
    assert pyramidification_cost(S, P) == 1
    S = 105
    P = [1, 6, 2, 5, 7]
    assert pyramidification_cost(S, P) == 3
    S = 10000
    P = [1, 6, 2, 5, 7]
    assert pyramidification_cost(S, P) == 999999991

# Print the sum of the pyramidification costs over all valid choices of L and R
print("Case #1:", pyramidification_cost(3000, [1, 6, 2, 5, 7]))
print("Case #2:", pyramidification_cost(500, [1, 6, 2, 5, 7]))
print("Case #3:", pyramidification_cost(106, [1, 6, 2, 5, 7]))
print("Case #4:", pyramidification_cost(105, [1, 6, 2, 5, 7]))
print("Case #5:", pyramidification_cost(10000, [1, 6, 2, 5, 7]))