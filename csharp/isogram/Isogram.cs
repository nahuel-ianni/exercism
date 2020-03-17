using System.Linq;

public static class Isogram
{
    public static bool IsIsogram(string word) 
    {
        word = word.ToLower().Replace("-", string.Empty).Replace(" ", string.Empty);

        return word.Length == word.Distinct().Count();    
    }
}
