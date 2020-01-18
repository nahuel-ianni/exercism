import unittest

from dna_transcription import to_dna

# Tests adapted from `problem-specifications//canonical-data.json` @ v1.3.0


class DnaTranscriptionTest(unittest.TestCase):
    def test_empty_dna_sequence(self):
        self.assertEqual(to_dna(""), "")

    def test_dna_complement_of_guanine_is_cytosine(self):
        self.assertEqual(to_dna("G"), "C")

    def test_dna_complement_of_cytosine_is_guanine(self):
        self.assertEqual(to_dna("C"), "G")

    def test_dna_complement_of_adenine_is_thymine(self):
        self.assertEqual(to_dna("A"), "T")

    def test_dna_complement_of_uracil_is_adenine(self):
        self.assertEqual(to_dna("U"), "A")

    def test_dna_complement(self):
        self.assertEqual(to_dna("UGCACCAGAAUU"), "ACGTGGTCTTAA")


if __name__ == "__main__":
    unittest.main()
