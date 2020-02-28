from re import sub
from string import punctuation


def count_words(sentence):
    word_count = {}
    sentence = sub(f"[{punctuation}]".replace("'", ""), " ", sentence.lower())
    sentence = [word.strip("'") for word in sentence.split()]

    for word in sentence:
        word_count[word] = sum(1 for w in sentence if w == word)

    return word_count
