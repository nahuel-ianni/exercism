using System;
using System.Collections.Generic;

public class Robot
{
    const string AllowedChars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    const int MaxDigit = 1000;

    public static IList<string> Names = new List<string>();

    Random random = new Random();

    public string Name
    {
        get;
        internal set;
    }

    public void Reset()
    {
        string name;

        do
        {
            var chars = $"{GetRandomChar()}{GetRandomChar()}";
            var digit = random.Next(MaxDigit).ToString("D3");

            name = $"{chars}{digit}";
        }
        while(Names.Contains(name));

        Names.Remove(Name);
        Names.Add(name);
        Name = name;
    }

    public Robot() => Reset();

    char GetRandomChar() =>
        AllowedChars[random.Next(AllowedChars.Length)];
}