export const recite = (initialBottlesCount, takeDownCount = 1) => {
  const lyrics = [];

  while (takeDownCount) {
    if (initialBottlesCount === 0) {
      lyrics.push(
        "No more bottles of beer on the wall, no more bottles of beer.",
        "Go to the store and buy some more, 99 bottles of beer on the wall.");

      break;
    }

    const bottles = getBottles(initialBottlesCount);
    lyrics.push(
      `${bottles} of beer on the wall, ${bottles} of beer.`,
      `Take ${initialBottlesCount - 1 ? 'one' : 'it'} down and pass it around, ${getBottles(initialBottlesCount - 1)} of beer on the wall.`);

    takeDownCount--;
    initialBottlesCount--;

    if (takeDownCount > 0)
      lyrics.push("");
  }

  return lyrics;
};

const getBottles = (number) => `${number ? number : 'no more'} ${number != 1 ? 'bottles' : 'bottle'}`;
