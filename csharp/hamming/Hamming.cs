using System;
using System.Linq;

public static class Hamming
{
    public static int Distance(string firstStrand, string secondStrand)
    {
        if (firstStrand.Length != secondStrand.Length)
            throw new ArgumentException("Strands are of different length.");

        return firstStrand.Zip(secondStrand, (c1, c2) => (c1 != c2)).Count(x => x);
    }
}