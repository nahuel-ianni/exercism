export class Matrix {
  m_cols;
  m_rows;

  constructor(values) { this.values = values; }

  get columns() {
    if (!this.m_cols)
      this.m_cols = this.rows[0].map((_, index) => this.rows.map(row => row[index]));

    return this.m_cols;
  }

  get rows() {
    if (!this.m_rows)
      this.m_rows = this.values.split("\n").map(row => row.match(/\d+/g).map(Number));

    return this.m_rows;
  }
}
