from re import sub
from string import punctuation


def abbreviate(words):
    words = sub(f"[{punctuation}]".replace("'", ""), " ", words.upper())

    return "".join(w[:1] for w in words.split())
