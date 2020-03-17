using System.Linq;

public static class Isogram
{
    public static bool IsIsogram(string word) 
    {
        return word.Where(c => char.IsLetter(c))
                   .Select(c => char.ToLower(c))
                   .GroupBy(c => c)
                   .All(group => group.Count() == 1);
    }
}
