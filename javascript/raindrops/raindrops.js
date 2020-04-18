export const convert = (raindrop) => {
  let sound = raindrop % 3 == 0 
    ? "Pling"
    : "";

  if (raindrop % 5 == 0)
    sound += "Plang";

  if (raindrop % 7 == 0)
    sound += "Plong";

  return sound 
    ? sound
    : raindrop.toString();
};
