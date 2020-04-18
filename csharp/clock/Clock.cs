using System;

public class Clock
{
    private int hours, minutes = 0;

    public Clock(int hours, int minutes)
    {
        var time = OffsetTime((hours * 60) + minutes);

        this.hours = time.Hours;
        this.minutes = time.Minutes;
    }

    public Clock Add(int minutesToAdd)
    {
        return new Clock(hours, minutes + minutesToAdd);
    }

    public Clock Subtract(int minutesToSub)
    {
        return new Clock(hours, minutes - Math.Abs(minutesToSub));
    }

    public override bool Equals(object obj) =>
        this.ToString() == obj.ToString();
    
    public override int GetHashCode() =>
        base.GetHashCode();

    public override string ToString() =>
        $"{hours.ToString("D2")}:{minutes.ToString("D2")}";

    private int HourOnTheDay(int minutes) =>
        (int)((decimal.Divide(minutes, 60)) % 24 + 24) % 24;

    private int MinuteOnTheHour(int minutes) =>
        ((minutes % 60) + 60) % 60;

    private (int Hours, int Minutes) OffsetTime(int offset)
    {
        var timespan = (hours * 60) + minutes + offset;

        return (HourOnTheDay(timespan), MinuteOnTheHour(timespan));
    }    
}
