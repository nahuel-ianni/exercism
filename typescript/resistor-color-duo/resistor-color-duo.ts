export class ResistorColor {
  private colors: string[];
  private table =
    [
      "black", "brown", "red", "orange", "yellow",
      "green", "blue", "violet", "grey", "white",
    ];

  constructor(colors: string[]) {
    if (colors.length < 2)
      throw new Error("At least two colors need to be present");

    this.colors = colors;
  }

  value = (): number => {
    const value1 = this.table.indexOf(this.colors[0]);
    const value2 = this.table.indexOf(this.colors[1]);

    if (value1 >= 0 && value2 >= 0)
      return 10 * value1 + value2;
    
    throw new Error("Not all requested colors were found");
  }
}
