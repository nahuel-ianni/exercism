export class Series {
  constructor(values) {
    this.values = [...values].map(Number);
  }

  get digits() { return this.values; }

  slices(length) {
    if (this.values.length < length)
      throw new Error("Slice size is too big.");

    const output = [];
    const limit = this.values.length - length;

    for (let index = 0; index <= limit; index++)
      output.push(this.values.slice(index, index + length));

    return output;
  }
}
