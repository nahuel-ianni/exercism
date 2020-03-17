using System.Linq;

public static class Pangram
{
    const int AlphabetLength = 26;

    public static bool IsPangram(string input) =>
        input.Where(c => char.IsLetter(c))
             .Select(c => char.ToLower(c))
             .GroupBy(c => c)
             .Count() == Pangram.AlphabetLength;
}
