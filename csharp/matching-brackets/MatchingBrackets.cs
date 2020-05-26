using System;
using System.Linq;
using System.Text.RegularExpressions;

public static class MatchingBrackets
{
    public static bool IsPaired(string input)
    {
        var curatedInput = input
            .Where(c => c.Equals('(') || c.Equals(')') ||
                        c.Equals('[') || c.Equals(']') ||
                        c.Equals('{') || c.Equals('}'));

        var brackets = string.Concat(curatedInput);

        while (brackets.Contains("()") || brackets.Contains("[]") || brackets.Contains("{}"))
            brackets = brackets.Replace("()", "").Replace("[]", "").Replace("{}", "");

        return brackets.Length == 0;
    }
}
