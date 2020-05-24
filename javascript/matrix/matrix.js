export class Matrix {
  constructor(values) {
    this.m_rows = values.split("\n").map(row => row.match(/\d+/g).map(Number));
    this.m_cols = this.m_rows[0].map((_, index) => this.m_rows.map(row => row[index]));
  }

  get columns() { return this.m_cols; }

  get rows() { return this.m_rows; }
}
