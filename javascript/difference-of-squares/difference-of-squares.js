export class Squares {
  constructor(upperBound) {
    this.upperBound = upperBound + 1;
  }

  get sumOfSquares() {
    let sum = 0;

    for (let i = 0; i < this.upperBound; i++)
      sum += Math.pow(i, 2);

    return sum;
  }

  get squareOfSum() {
    let sum = 0;

    for (let i = 0; i < this.upperBound; i++)
      sum += i;

    return Math.pow(sum, 2);
  }

  get difference() {
    return this.squareOfSum- this.sumOfSquares;
  }

  get numbers() {
    return new Array().fill();
  }
}
