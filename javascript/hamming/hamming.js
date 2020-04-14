export const compute = (s1, s2) => {
  if (s1.length == 0 && s2.length != 0)
    throw new Error("left strand must not be empty");

  else if (s1.length != 0 && s2.length == 0)
    throw new Error("right strand must not be empty");

  else if (s1.length != s2.length)
    throw new Error("left and right strands must be of equal length");

  let diff = 0;
  for (let i = 0; i < s1.length; i++)
    if (s1[i] != s2[i])
      diff++;

  return diff;
};
