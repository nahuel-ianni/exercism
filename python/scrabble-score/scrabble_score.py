score_table = {
    "AEIOULNRST" : 1,
    "DG"         : 2,
    "BCMP"       : 3,
    "FHVWY"      : 4,
    "K"          : 5,
    "JX"         : 8,
    "QZ"         : 10
}


def score(word):
    return sum(value 
                for ch in word.upper() 
                for key, value in score_table.items() 
                if ch in key)
