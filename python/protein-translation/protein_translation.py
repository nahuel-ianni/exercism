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
    "UAA": "STOP",
    "UAG": "STOP",
    "UGA": "STOP",
}

def proteins(strand):
    if len(strand) % 3 != 0:
        raise ValueError("Unsupported operation: The strand info doesn't allow creating proper length codons (3 char long).")

    codons = [strand[i:i+3] for i in range(0, len(strand), 3)]
    amino_acids = [amino_acid.get(c) for c in codons]

    return amino_acids if "STOP" not in amino_acids else amino_acids[:amino_acids.index("STOP")]
