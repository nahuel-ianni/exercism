export class Triplet {
  constructor(a, b, c) {
    this.sum = () => a + b + c;
    this.product = () => a * b * c;
    this.isPythagorean = () => a ** 2 + b ** 2 === c ** 2 && a < b < c;
  }

  static where({ maxFactor, minFactor = 1, sum = null }) {
    const triplets = [];

    for (let i = minFactor; i <= maxFactor; ++i)
      for (let j = i + 1; j <= maxFactor; ++j)
        for (let k = j + 1; k <= maxFactor; ++k) {
          const triplet = new Triplet(i, j, k);

          if (sum && triplet.sum() !== sum)
            continue;

          if (triplet.isPythagorean())
            triplets.push(triplet);
        }

    return triplets;
  }
}
