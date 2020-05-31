export class Squares {
  constructor(upperBound) {
    this.numbers = [...Array(upperBound + 1).keys()];
  }

  get sumOfSquares() {
    return this.numbers
      .map(x => Math.pow(x, 2))
      .reduce((x, y) => x + y, 0);
  }

  get squareOfSum() {
    return Math.pow(this.numbers.reduce((x, y) => x + y, 0), 2);
  }

  get difference() {
    return this.squareOfSum - this.sumOfSquares;
  }
}