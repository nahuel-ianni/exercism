def to_rna(dna_strand):
    nucleotide_complements = {
        "G": "C",
        "C": "G",
        "T": "A",
        "A": "U",
    }

    return "".join([nucleotide_complements.get(n) for n in dna_strand])


def to_dna(rna_strand):
    nucleotide_complements = str.maketrans("CGAU", "GCTA")
    
    return rna_strand.translate(nucleotide_complements)
