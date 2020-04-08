public class Clock
{
    private int hours, minutes = 0;

    public Clock() { }

    public Clock(int hours, int minutes)
    {
        var time = OffsetTime(HoursToMinutes(hours) + minutes);

        this.hours = time.Hours;
        this.minutes = time.Minutes;
    }

    public Clock Add(int minutesToAdd)
    {
        var time = OffsetTime(minutesToAdd);

        return new Clock()
        {
            hours = time.Hours,
            minutes = time.Minutes
        };
    }

    public Clock Subtract(int minutesToSub)
    {
        var time = OffsetTime(
            minutesToSub > 0
                ? minutesToSub * -1
                : minutesToSub);

        return new Clock()
        {
            hours = time.Hours,
            minutes = time.Minutes
        };
    }

    public override bool Equals(object obj) =>
        this.ToString() == obj.ToString();

    public override string ToString() =>
        $"{hours.ToString("D2")}:{minutes.ToString("D2")}";

    private int HourOnTheDay(int minutes) =>
        (int)((decimal.Divide(minutes, 60)) % 24 + 24) % 24;

    private int HoursToMinutes(int hours) =>
        hours * 60;

    private int MinuteOnTheHour(int minutes) =>
        ((minutes % 60) + 60) % 60;

    private (int Hours, int Minutes) OffsetTime(int offset)
    {
        var timespan = HoursToMinutes(hours) + minutes + offset;

        return (HourOnTheDay(timespan), MinuteOnTheHour(timespan));
    }
}
