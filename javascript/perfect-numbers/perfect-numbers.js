export const classify = (number) => {
  if (number < 1)
    throw new Error('Classification is only possible for natural numbers.');

  const arrayLimit = Math.floor(number / 2) + 1;
  const aliquotSum = [...Array(arrayLimit).keys()].reduce(
    (accumulator, currentValue) =>
      number % currentValue === 0
        ? accumulator + currentValue
        : accumulator
  );

  if (aliquotSum === number)
    return 'perfect';

  else if (aliquotSum > number)
    return 'abundant';

  else
    return 'deficient';
};
