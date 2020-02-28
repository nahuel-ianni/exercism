from re import sub
from string import punctuation


def count_words(sentence):
    word_count = {}
    sentence = sub(f"[{punctuation}]".replace("'", ""), " ", sentence.lower())

    for word in sentence.split():
        word = word.strip("'")
        word_count[word] = sum(1 for w in sentence.split() if w.strip("'") == word)

    return word_count
