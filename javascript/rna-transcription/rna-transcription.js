const dnaTranscription = {
  "G": "C",
  "C": "G",
  "T": "A",
  "A": "U"
}

export const toRna = (dna) => {
  let rna = "";

  for (const ch of dna)
    rna += dnaTranscription[ch];

  return rna;
};
