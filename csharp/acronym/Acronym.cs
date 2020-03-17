using System;
using System.Linq;

public static class Acronym
{
    static char[] delimiterChars = { ' ', '-', '_' };

    public static string Abbreviate(string phrase) =>
        string.Concat(
            from word in phrase.Split(delimiterChars, StringSplitOptions.RemoveEmptyEntries)
            select word.Substring(0, 1).ToUpper());
}