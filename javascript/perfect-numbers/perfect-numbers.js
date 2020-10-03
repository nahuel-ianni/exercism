export const classify = (number) => {
  if (number < 1)
    throw new Error('Classification is only possible for natural numbers.');

  const aliquotSum = [...Array(Math.floor(number / 2) + 1).keys()].reduce(
    (accumulator, currentValue) =>
      number % currentValue === 0
        ? accumulator + currentValue
        : accumulator
  );

  if (aliquotSum === number)
    return 'perfect';

  else
    return aliquotSum > number ? 'abundant' : 'deficient';
};
