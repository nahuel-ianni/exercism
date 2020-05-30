export const valid = (card_number) => {
  card_number = card_number?.split(' ').join('');
  let digits = card_number?.match(/\d+/g).join('');

  if (!card_number || card_number.length <= 1 || digits != card_number)
    return false;

  digits = digits.split('').map(x => Number(x));

  for (let i = digits.length - 2; i >= 0; i -= 2) {
    const digit = digits[i] * 2;
    digits[i] = digit < 10 ? digit : digit - 9;
  }

  return digits.reduce((a, b) => a + b, 0) % 10 === 0;
};
