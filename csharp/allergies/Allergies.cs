using System;
using System.Collections.Generic;
using System.Linq;

/// Used whenever the enumerable represents a collection of 
/// possible values, rather than a single value. 
/// Such collections are often used with bitwise operators.
[Flags]
public enum Allergen
{
    Eggs         = 1,
    Peanuts      = 2,
    Shellfish    = 4,
    Strawberries = 8,
    Tomatoes     = 16,
    Chocolate    = 32,
    Pollen       = 64,
    Cats         = 128
}

public class Allergies
{
    private readonly IEnumerable<Allergen> allergens = 
        Enum.GetValues(typeof(Allergen)).Cast<Allergen>();
    private readonly Allergen mask;

    public Allergies(int mask) =>
        this.mask = (Allergen)mask;

    public bool IsAllergicTo(Allergen allergen) =>
        mask.HasFlag(allergen);

    public Allergen[] List() =>
        allergens.Where(IsAllergicTo).ToArray();
}