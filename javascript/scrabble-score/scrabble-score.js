const scoreTable = new Map([
  [1, ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T']],
  [2, ['D', 'G']],
  [3, ['B', 'C', 'M', 'P']],
  [4, ['F', 'H', 'V', 'W', 'Y']],
  [5, ['K']],
  [8, ['J', 'X']],
  [10, ['Q', 'Z']]
]);

export const score = (word) => [...word].reduce(reducer, 0);

const reducer = (accumulator, char) => {
  const value = [...scoreTable.entries()].find(({ 1: v }) => v.includes(char.toUpperCase()))[0];

  return accumulator + value;
}