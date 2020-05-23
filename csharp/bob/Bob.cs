using System.Linq;

public static class Bob
{
    public static string Response(string statement)
    {
        statement = statement.Trim();
        var isYelling = IsYelling(statement);
        var output = "Whatever.";

        if (IsSilent(statement))
            output = "Fine. Be that way!";

        else if (IsQuestion(statement))
            output = isYelling
                ? "Calm down, I know what I'm doing!"
                : "Sure.";

        else if (isYelling)
            output = "Whoa, chill out!";

        return output;
    }

    private static bool IsQuestion(string s) =>
        s.EndsWith("?");

    private static bool IsSilent(string s) =>
        string.IsNullOrEmpty(s);

    private static bool IsYelling(string s) =>
        s.Any(c => char.IsLetter(c)) &&
        s.Where(c => char.IsLetter(c)).All(c => char.IsUpper(c));
}