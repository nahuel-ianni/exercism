export const reverseString = (sequence) => {
  let output = "";

  for (let i = sequence.length - 1; i >= 0; i--)
    output += sequence[i];

  return output;
};
