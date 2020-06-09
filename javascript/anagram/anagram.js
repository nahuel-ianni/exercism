export const findAnagrams = (word, candidates) => {
  word = word.toLowerCase();
  const chars = [...word].sort().join();

  return candidates
    .filter(x =>
      x.toLowerCase() !== word &&
      chars === [...x.toLowerCase()].sort().join()
    );
}
