export const isArmstrongNumber = (num) => {
  const value = `${num}`;
  const power = value.length;
  let formula = 0;

  value.split("").forEach(x => formula += x**power);
  return formula == num;
};
