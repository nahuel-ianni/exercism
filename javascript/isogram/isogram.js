export const isIsogram = (phrase) => {
  const characters = [...sanitizePhrase(phrase)];
  const set = new Set(characters);

  return characters.length === set.size;
};

const sanitizePhrase = (phrase) => {
  return phrase
    .toLowerCase()
    .replace(' ', '')
    .replace('-', '');
}
