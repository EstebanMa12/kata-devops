from typing import Union


def concatenate_nth_letters(words: Union[list, tuple]) -> str:
    if words is None:
        raise TypeError("words must not be None")
    if isinstance(words, (str, bytes)):
        raise TypeError("words must be a list or tuple of strings, not str or bytes")
    if not isinstance(words, (list, tuple)):
        raise TypeError("words must be a list or tuple")

    parts: list[str] = []
    for n, word in enumerate(words):
        if not isinstance(word, str):
            continue
        if len(word) > n:
            parts.append(word[n])
    return "".join(parts)
