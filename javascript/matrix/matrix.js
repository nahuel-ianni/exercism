export class Matrix {
  constructor(values) {
    this.m_columns, this.m_rows = new Array();

    values.split("\n").forEach(row => {
      this.m_rows.push(row.match(/\d+/g).map(Number));
    });
  }

  get columns() { return this.m_columns; }

  get rows() { return this.m_rows; }
}
