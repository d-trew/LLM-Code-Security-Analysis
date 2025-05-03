from typing import List, Tuple

def get_minimum_parentheses(s: str) -> str:
    """
    Return a new string with minimum number of opening and closing parentheses.

    Parameters:
        s (str): Input string.

    Returns:
        (str): A new string with minimum number of opening and closing parentheses.
    """
    result = []
    nesting_depth = 0
    for char in s:
        if char == "(":
            nesting_depth += 1
            result.append(char)
        elif char == ")":
            nesting_depth -= 1
            result.append(char)
        else:
            result.append(char)
    while nesting_depth > 0:
        result.append(")")
        nesting_depth -= 1
    return "".join(result[::-1])

def get_minimum_parentheses_solution(s: str) -> Tuple[str, int]:
    """
    Return a new string with minimum number of opening and closing parentheses.

    Parameters:
        s (str): Input string.

    Returns:
        (Tuple[str, int]): A tuple containing the new string with minimum number of opening and closing parentheses and its length.
    """
    result = get_minimum_parentheses(s)
    return result, len(result)

def solve(s: str) -> Tuple[str, int]:
    """
    Return a new string with minimum number of opening and closing parentheses.

    Parameters:
        s (str): Input string.

    Returns:
        (Tuple[str, int]): A tuple containing the new string with minimum number of opening and closing parentheses and its length.
    """
    result = get_minimum_parentheses(s)
    return result, len(result)

def main() -> None:
    """
    Read input from stdin, call solve function, and print output to stdout.
    :return: None
    """
    test_cases = int(input())
    results = []
    for i in range(test_cases):
        s = input()
        result = solve(s)
        results.append(result)
    for result in results:
        print(f"Case #{i+1}: {result[0]}")

if __name__ == "__main__":
    main()