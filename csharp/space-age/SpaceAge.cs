using System;

public class SpaceAge
{
    readonly double spaceAgeOnEarth, spaceAgeOnMercury, spaceAgeOnVenus, 
                    spaceAgeOnMars, spaceAgeOnJupiter, spaceAgeOnSaturn, 
                    spaceAgeOnUranus, spaceAgeOnNeptune;

    public SpaceAge(int seconds)
    {
        var yearlySecondsOnEarth = 31557600;

        spaceAgeOnEarth   = CalculateYears(seconds, yearlySecondsOnEarth);
        spaceAgeOnMercury = CalculateYears(seconds, 0.2408467  * yearlySecondsOnEarth);
        spaceAgeOnVenus   = CalculateYears(seconds, 0.61519726 * yearlySecondsOnEarth);
        spaceAgeOnMars    = CalculateYears(seconds, 1.8808158  * yearlySecondsOnEarth);
        spaceAgeOnJupiter = CalculateYears(seconds, 11.862615  * yearlySecondsOnEarth);
        spaceAgeOnSaturn  = CalculateYears(seconds, 29.447498  * yearlySecondsOnEarth);
        spaceAgeOnUranus  = CalculateYears(seconds, 84.016846  * yearlySecondsOnEarth);
        spaceAgeOnNeptune = CalculateYears(seconds, 164.79132  * yearlySecondsOnEarth);
    }

    public double OnEarth() => spaceAgeOnEarth;
    public double OnMercury() => spaceAgeOnMercury;
    public double OnVenus() => spaceAgeOnVenus;
    public double OnMars() => spaceAgeOnMars;
    public double OnJupiter() => spaceAgeOnJupiter;
    public double OnSaturn() => spaceAgeOnSaturn;
    public double OnUranus() => spaceAgeOnUranus;
    public double OnNeptune() => spaceAgeOnNeptune;

    private static double CalculateYears(int seconds, double planetarySeconds) =>
        Math.Round(seconds / planetarySeconds, 2);
}