def analyze_text(text):
    """Analyzes text to count word occurrences and identify the longest word.

    Args:
      text: The input text string.

    Returns:
      A dictionary containing:
        - word_counts: A dictionary where keys are words (lowercase) and values are their counts.
        - longest_word: The longest word in the text (lowercase).  Returns "" if the text is empty.

    """
    if not text:
        return {"word_counts": {}, "longest_word": ""}

    words = text.lower().split()
    word_counts = {}
    longest_word = ""

    for word in words:
        cleaned_word = ''.join(c for c in word if c.isalnum()) #remove punctuation
        if cleaned_word: #skip empty strings after punctuation removal
            word_counts[cleaned_word] = word_counts.get(cleaned_word, 0) + 1
            if len(cleaned_word) > len(longest_word):
                longest_word = cleaned_word

    return {"word_counts": word_counts, "longest_word": longest_word}