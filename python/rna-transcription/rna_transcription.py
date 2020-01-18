def to_rna(dna_strand):
    nucleotide_complements = {
        "G": "C",
        "C": "G",
        "T": "A",
        "A": "U",
    }

    return "".join([nucleotide_complements.get(n) for n in dna_strand])


def to_dna(rna_strand):
    """ This method was added by me to keep two different solutions in the same place for future references. """
    """ New tests were added for the method. """
    
    nucleotide_complements = str.maketrans("CGAU", "GCTA")
    
    return rna_strand.translate(nucleotide_complements)
