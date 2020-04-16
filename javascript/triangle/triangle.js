export class Triangle {
  constructor(a, b, c) {
    this.sides = [a, b, c].sort();
  }

  isEquilateral() {
    return this._guard_shape() && [...new Set(this.sides)].length == 1;
  }

  isIsosceles() {
    return this._guard_shape() && [1, 2].includes([...new Set(this.sides)].length);
  }

  isScalene() {
    return this._guard_shape() && [...new Set(this.sides)].length == 3;
  }

  _guard_shape(){
    return this.sides.every((x) => x > 0) &&
           this.sides[0] + this.sides[1] >= this.sides[2];
  }
}
