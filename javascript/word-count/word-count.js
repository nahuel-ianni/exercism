export const countWords = (phrase) => {
  const words = Object.create(null);
  phrase = phrase.toLowerCase().match(/([\w]+['][\w]+)|\w+/g);

  phrase.forEach(word => {
    if (words[word]) words[word] += 1;
    else words[word] = 1;
  });

  return words;
};
