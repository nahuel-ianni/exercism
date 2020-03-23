using System;
using System.Collections.Generic;

public class Robot
{
    const string AllowedChars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    const int AllowedUpperLimitDigit = 1000;

    public static IList<string> Names = new List<string>();

    public string Name { get; private set; }

    public Robot() => Reset();

    public void Reset()
    {
        var random = new Random();
        var formerName = Name;

        do
        {
            Name = string.Format(
                "{0}{1}{2}",
                AllowedChars[random.Next(AllowedChars.Length)],
                AllowedChars[random.Next(AllowedChars.Length)],
                random.Next(AllowedUpperLimitDigit).ToString("D3"));
        }
        while (Names.Contains(Name));

        Names.Remove(formerName);
        Names.Add(Name);
    }
}