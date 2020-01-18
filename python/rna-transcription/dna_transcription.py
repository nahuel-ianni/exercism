def to_dna(rna_strand):
    """ This class was added by me to keep two different solutions to the original exercise for future references. """
    """ New tests were added for the class. """
    
    nucleotide_complements = str.maketrans("CGAU", "GCTA")
    
    return rna_strand.translate(nucleotide_complements)
