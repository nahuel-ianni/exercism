const scoreTable = {
  1: ['a', 'e', 'i', 'o', 'u', 'l', 'n', 'r', 's', 't'],
  2: ['d', 'g'],
  3: ['b', 'c', 'm', 'p'],
  4: ['f', 'h', 'v', 'w', 'y'],
  5: ['k'],
  8: ['j', 'x'],
  10: ['q', 'z']
};

const getScore = (char) => {
  for (let value in scoreTable)
    if (scoreTable[value].includes(char)) return Number(value);
}

export const score = (word) =>
  [...word]
    .map(char => getScore(char.toLowerCase()))
    .reduce((sum, value) => { return sum + value }, 0);