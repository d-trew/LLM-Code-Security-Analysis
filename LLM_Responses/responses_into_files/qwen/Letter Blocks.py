def can_stack_towers(towers):
    from collections import Counter

    def is_valid_megatower(megatower):
        letter_counts = Counter(megatower)
        for letter in set(megatower):
            if letter not in letter_counts:
                continue
            start_index = megatower.index(letter)
            end_index = len(megatower) - 1 - megatower[::-1].index(letter)
            if any(megatower[i] != letter for i in range(start_index + 1, end_index)):
                return False
        return True

    def combine_towers(towers):
        from itertools import permutations

        min_length = float('inf')
        best_megatower = None
        for perm in permutations(towers):
            megatower = ''.join(perm)
            if is_valid_megatower(megatower) and len(megatower) < min_length:
                min_length = len(megatower)
                best_megatower = megatower
        return best_megatower

    for i, towers in enumerate(towers):
        result = combine_towers(towers)
        if result is None:
            print(f"Case #{i+1}: IMPOSSIBLE")
        else:
            print(f"Case #{i+1}: {result}")

# Example usage:
towers = [
    ["JAMMICCODEEELZZZZZ", "ZZZZZJAMMICCODEEEL"],
    ["H", "EEK", "HASH", "EEK"],
    ["OOY", "YYO"],
    ["HH", "HS"],
    ["AA", "BB", "CC"],
    ["A", "B"]
]

can_stack_towers(towers)