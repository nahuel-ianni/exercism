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

        // this.minutes = minutes >= 0
        //     ? minutes % 60
        //     : 60 - ((minutes * -1) % 60);

        // this.hours = hours >= 0
        //     ? (hours + minutes / 60) % 24
        //     : 24 - ((hours * -1) % 24);
    }

    public Clock Add(int minutes)
    {
        this.minutes += minutes % 60;
        this.hours += (minutes / 60) % 24;

        return this;
    }

    public Clock Subtract(int minutes)
    {
        this.minutes = (60 - (minutes * -1)) % 60;
        this.hours = (24 - (((minutes * -1) / 60) % 24)) % 24;

        return this;
    }

    public override bool Equals(object obj) =>
        this.ToString() == obj.ToString();

    public override string ToString() =>
        $"{hours.ToString("D2")}:{minutes.ToString("D2")}";
}
