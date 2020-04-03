using System.Linq;

public static class RotationalCipher
{
    public static string Rotate(string text, int shiftKey)
    {
        return string.Concat(
            from ch in text
            select char.IsLetter(ch)
                ? ProcessOffset(ch, shiftKey)
                : ch);
    }

    private static char ProcessOffset(char ch, int offset)
    {
        var c = (int)ch;
        var lowerBound = (int)(char.IsUpper(ch) ? 'A' : 'a');

        return (char)(lowerBound + (c - lowerBound + offset) % 26);
    }
}

// private static List<char> Alphabet = new List<char> {
//     'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
//     'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
//     'W', 'X', 'Y', 'Z'
// };

// public static string Rotate(string text, int shiftKey)
// {
//     var sb = new StringBuilder();
//     var alphabet =
//         Alphabet.GetRange(shiftKey, Alphabet.Count - shiftKey)
//                 .Concat(Alphabet.GetRange(0, shiftKey));

//     foreach (var ch in text)
//     {
//         sb.Append(
//             char.IsLetter(ch)
//                 ? char.IsLower(ch) 
//                     ? char.ToLower(alphabet.ElementAt(Alphabet.IndexOf(char.ToUpper(ch)))) 
//                     : alphabet.ElementAt(Alphabet.IndexOf(ch))
//                 : ch
//         );
//     }

//     return sb.ToString();
// }