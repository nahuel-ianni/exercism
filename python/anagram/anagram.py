def find_anagrams(word, candidates):
    word = word.lower()
    
    return [w for w in candidates if len(w) == len(word) and w.lower() != word and sorted(w.lower()) == sorted(word)]
