const dnaTranscription = {
  "G": "C",
  "C": "G",
  "T": "A",
  "A": "U"
}

export const toRna = (dna) => {
  let rna = "";

  if (dna.length == 0)
    return rna;

  dna.split("").forEach(element => {
    rna += dnaTranscription[element];
  });

  return rna;
};
