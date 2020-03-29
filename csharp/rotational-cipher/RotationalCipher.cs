using System;
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
        /// Uppercase letters: ASCII A to Z = 65 to 90
        /// Lowercase letters: ASCII a to z = 97 to 122
        var b = Convert.ToByte(ch);
        var lowerBound = b <= 90 ? 65 : 97;
        var upperBound = b <= 90 ? 90 : 122;

        var position = (b + offset) > upperBound
            ? lowerBound + ((b + offset) - upperBound) - 1
            : b + offset;

        return Convert.ToChar(position);
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