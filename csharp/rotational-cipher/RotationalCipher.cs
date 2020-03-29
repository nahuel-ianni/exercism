using System;
using System.Collections.Generic;
using System.Linq;

public static class RotationalCipher
{
    private static List<char> Alphabet = new List<char> {
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
        'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
        'W', 'X', 'Y', 'Z'
    };

    public static string Rotate(string text, int shiftKey)
    {
        return String.Concat(
                from ch in text
                select char.IsLetter(ch)
                    ? ProcessOffset(ch, shiftKey)       //Convert.ToByte(ch), shiftKey)
                    : ch);
    }

    private static char ProcessOffset(char ch, int offset)
    {
        var alphabet = 
            Alphabet.GetRange(offset, Alphabet.Count - offset)
                    .Concat(Alphabet.GetRange(0, offset));

        return char.IsLower(ch) 
                ? char.ToLower(alphabet.ElementAt(char.ToUpper(ch))) 
                : alphabet.ElementAt(ch);
    }

    // private static char ProcessOffset(byte b, int offset)
    // {
    //     /// Uppercase letters = ASCII 65 to 90
    //     /// Lowercase letters = ASCII 97 to 122
    //     var lowerBound = b <= 90 ? 65 : 97;
    //     var upperBound = b <= 90 ? 90 : 122;

    //     var position = (b + offset) > upperBound
    //         ? 0
    //         : 0;

    //     return Convert.ToChar(position);
    // }
}