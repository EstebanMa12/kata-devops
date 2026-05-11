def concatenate_nth_letters(words: list) -> str:
    return "".join(word[n] for n, word in enumerate(words) if len(word) > n)
