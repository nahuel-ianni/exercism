export class ResistorColor {
  private colors: string[];
  private table = new Map<string, number>(
    [
      [ "black" , 0 ],
      [ "brown" , 1 ],
      [ "red"   , 2 ],
      [ "orange", 3 ],
      [ "yellow", 4 ],
      [ "green" , 5 ],
      [ "blue"  , 6 ],
      [ "violet", 7 ],
      [ "grey"  , 8 ],
      [ "white" , 9 ],
    ]);

  constructor(colors: string[]) {
    if (colors.length < 2)
      throw new Error("At least two colors need to be present");

    this.colors = colors;
  }

  value = (): number => {
    const value1 = this.table.get(this.colors[0]);
    const value2 = this.table.get(this.colors[1]);

    if (value1 != null && value2 != null)
      return 10 * value1 + value2;
    
    throw new Error("Not all requested colors were found");
  }
}
