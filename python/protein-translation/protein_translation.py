from textwrap import wrap
from itertools import takewhile

amino_acid = {
    "AUG": "Methionine",
    "UUU": "Phenylalanine",
    "UUC": "Phenylalanine",
    "UUA": "Leucine",
    "UUG": "Leucine",
    "UCU": "Serine",
    "UCC": "Serine",
    "UCA": "Serine",
    "UCG": "Serine",
    "UAU": "Tyrosine",
    "UAC": "Tyrosine",
    "UGU": "Cysteine",
    "UGC": "Cysteine",
    "UGG": "Tryptophan",
    "UAA": None,
    "UAG": None,
    "UGA": None,
}

def proteins(strand):
    codons = wrap(strand, 3)                                    # [strand[i:i+3] for i in range(0, len(strand), 3)]
    amino_acids = [amino_acid.get(c) for c in codons]

    return list(takewhile(lambda x: x, amino_acids))            # amino_acids if "STOP" not in amino_acids else amino_acids[:amino_acids.index("STOP")]
