export class Clock {
  hours = 0;
  minutes = 0;

  constructor(hours, minutes = 0) {
    const time = this.offsetTime((hours * 60) + minutes);

    this.hours = time[0];
    this.minutes = time[1];
  }

  toString() {
    return `${this.hours.toString().padStart(2, "0")}:${this.minutes.toString().padStart(2, "0")}`;
  }

  plus(offset) {
    return new Clock(
      this.hours, 
      this.minutes + offset);
  }

  minus(offset) {
    return new Clock(
      this.hours, 
      this.minutes - Math.abs(offset));
  }

  equals(other) {
    return this.toString() == other.toString();
  }

  offsetTime(offset) {
    const timespan = (this.hours * 60) + this.minutes + offset;

    return [
      Math.floor(((timespan / 60) % 24 + 24) % 24),
      Math.floor(((timespan % 60) + 60) % 60)
    ];
  }
}
