using System;

public class SpaceAge
{
    const int yearlySecondsOnEarth = 31557600;
    const double planetarySecondsMercury = 0.2408467 * yearlySecondsOnEarth;
    const double planetarySecondsVenus   = 0.61519726 * yearlySecondsOnEarth;
    const double planetarySecondsMars    = 1.8808158 * yearlySecondsOnEarth;
    const double planetarySecondsJupiter = 11.862615 * yearlySecondsOnEarth;
    const double planetarySecondsSaturn  = 29.447498 * yearlySecondsOnEarth;
    const double planetarySecondsUranus  = 84.016846 * yearlySecondsOnEarth;
    const double planetarySecondsNeptune = 164.79132 * yearlySecondsOnEarth;

    readonly int seconds;

    public SpaceAge(int seconds) => 
        this.seconds = seconds;

    public double OnEarth() => this.CalculateYears(yearlySecondsOnEarth);

    public double OnMercury() => this.CalculateYears(planetarySecondsMercury);

    public double OnVenus() => this.CalculateYears(planetarySecondsVenus);

    public double OnMars() => this.CalculateYears(planetarySecondsMars);

    public double OnJupiter() => this.CalculateYears(planetarySecondsJupiter);

    public double OnSaturn() => this.CalculateYears(planetarySecondsSaturn);

    public double OnUranus() => this.CalculateYears(planetarySecondsUranus);

    public double OnNeptune() => this.CalculateYears(planetarySecondsNeptune);

    private double CalculateYears(double planetarySeconds)
    {
        return Math.Round(this.seconds / planetarySeconds, 2);
    }
}