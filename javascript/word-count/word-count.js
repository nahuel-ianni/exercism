export const countWords = (phrase) => {
  const words = {};
  phrase
    .toLowerCase()
    .match(/\w+('\w)?/g)
    .forEach(word => 
      words[word]++ || (words[word] = 1));

  return words;
};
