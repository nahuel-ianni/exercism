export const transform = (oldTable) => {
  const scoreTable = {};

  for (const score in oldTable) {
    oldTable[score].forEach(ch =>
      scoreTable[ch.toLowerCase()] = Number(score));
  }

  return scoreTable;
};
