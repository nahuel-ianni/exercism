using System;

public static class Gigasecond
{
    // Math.Pow(10, 9) == 1e9
    public static DateTime Add(DateTime moment) => moment.AddSeconds(1e9);
}