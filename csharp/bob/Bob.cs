using System.Linq;

public static class Bob
{
    public static string Response(string statement)
    {
        statement = statement.Trim();
        var isUpper = IsUpper(statement);
        var output = "Whatever.";

        if (string.IsNullOrEmpty(statement))
            output = "Fine. Be that way!";

        else if (statement.EndsWith("?"))
            output = isUpper
                ? "Calm down, I know what I'm doing!"
                : "Sure.";

        else if (isUpper)
            output = "Whoa, chill out!";

        return output;
    }

    private static bool IsUpper(string s)
    {
        return s.Any(c => char.IsLetter(c)) &&
               s.Where(c => char.IsLetter(c)).All(c => char.IsUpper(c));
    }
}