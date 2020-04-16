export const steps = (num, count = 0) => {
  if (num <= 0)
    throw new Error("Only positive numbers are allowed");

  if (num == 1)
    return count;

  return num % 2 == 0
    ? steps(num / 2, ++count)
    : steps((num * 3) + 1, ++count);
};
