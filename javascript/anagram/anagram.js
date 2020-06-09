export const findAnagrams = (word, candidates) => {
  word = word.toLowerCase();
  const chars = [...word].sort().join();

  return candidates
    .filter(x => 
      x.length === word.length &&
      x.toLowerCase() !== word &&
      chars === [...x.toLowerCase()].sort().join()
    );
}
