using System;
using System.Linq;
using System.Collections.Generic;

public static class NucleotideCount
{
    const string ValidNucletoides = "ACGT";

    public static IDictionary<char, int> Count(string sequence)
    {
        if (sequence.Except(ValidNucletoides).Count() > 0)
            throw new ArgumentException("Sequence contains invalid characters.");
        
        return ValidNucletoides
                .Select(x => new KeyValuePair<char, int>(x, sequence.Count(y => y == x)))
                .ToDictionary(t => t.Key, t => t.Value);
    }
}