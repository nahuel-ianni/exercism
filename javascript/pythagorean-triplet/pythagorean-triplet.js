export class Triplet {
  constructor(a, b, c) {
    this.a = a;
    this.b = b;
    this.c = c;
  }

  sum = () => this.a + this.b + this.c;

  product = () => this.a * this.b * this.c;

  isPythagorean = () =>
    this.a ** 2 + this.b ** 2 === this.c ** 2 &&
    this.a < this.b < this.c;

  static where({ maxFactor, minFactor = 1, sum = -1 }) {
    const triplets = [];

    for (let i = minFactor; i <= maxFactor; ++i) {
      for (let j = i + 1; j <= maxFactor; ++j) {
        for (let k = j + 1; k <= maxFactor; ++k) {
          const triplet = new Triplet(i, j, k);

          if (sum !== -1 && triplet.sum() !== sum)
            continue;

          if (triplet.isPythagorean())
            triplets.push(triplet);
        }
      }
    }

    return triplets;
  }
}
