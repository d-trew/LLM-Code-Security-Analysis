def max_unique_characters(test_cases):
    results = []
    for i, (text, n, replacements) in enumerate(test_cases, start=1):
        unique_chars = set(text)
        for a, b in replacements:
            if a in text or b in text:
                unique_chars |= {c for c in text if c == a or c == b}
        results.append(f"Case #{i}: {len(unique_chars)}")
    return results

# Example usage
test_cases = [
    ("CODEJAMWORLDFINALS", 2, [('A', 'O'), ('O', 'Y')]),
    ("1234567890", 1, [('1', 'A')]),
    ("ABCD", 2, [('A', 'B'), ('C', 'D')]),
    ("Xx", 2, [('X', 'a'), ('x', 'b')])
]

results = max_unique_characters(test_cases)
for result in results:
    print(result)