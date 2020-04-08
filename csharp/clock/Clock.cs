using System;

public class Clock
{
    private int hours, minutes = 0;

    public Clock(int hours, int minutes)
    {
        _ = hours >= 0
            ? Add(hours * 60)
            : Subtract(hours * 60);

        _ = minutes >= 0
            ? Add(minutes)
            : Subtract(minutes);
    }

    private int HoursToMinutes(int hours) =>
        hours * 60;

    private int MinuteOnTheHour(int minutes) =>
        minutes >= 0
            ? minutes % 60
            : minutes % 60 + 60;

    private int HourOnTheDay(int minutes) =>
        (int)((decimal.Divide(minutes, 60)) % 24 + 24) % 24;
        
        // minutes >= 0
        //     ? (minutes / 60) % 24
        //     : (int)((decimal.Divide(minutes, 60)) % 24 + 24) % 24;           //: (int)Math.Ceiling(decimal.Divide(minutes, 60)) % 24 + 24;     // (minutes / 60) % 24 + 24;

    public Clock Add(int minutesToAdd)
    {
        minutes = MinuteOnTheHour(minutes + MinuteOnTheHour(minutesToAdd));
        hours = HourOnTheDay(HoursToMinutes(hours + HourOnTheDay(minutesToAdd)));

        return this;
    }

    public Clock Subtract(int minutesToSub)
    {
        minutes = MinuteOnTheHour(minutes + MinuteOnTheHour(minutesToSub));
        hours = HourOnTheDay(HoursToMinutes(hours + HourOnTheDay(minutesToSub)));

        return this;
    }

    public override bool Equals(object obj) =>
        this.ToString() == obj.ToString();

    public override string ToString() =>
        $"{hours.ToString("D2")}:{minutes.ToString("D2")}";
}
