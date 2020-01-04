import string


def is_pangram(sentence):
    alphabet = set(string.ascii_lowercase)
    sentence = set(sentence.lower())

    return sentence >= alphabet
