using System;

public class SpaceAge
{
    const double orbitalPeriodEarth   = 1;
    const double orbitalPeriodMercury = 0.2408467;
    const double orbitalPeriodVenus   = 0.61519726;
    const double orbitalPeriodMars    = 1.8808158;
    const double orbitalPeriodJupiter = 11.862615;
    const double orbitalPeriodSaturn  = 29.447498;
    const double orbitalPeriodUranus  = 84.016846;
    const double orbitalPeriodNeptune = 164.79132;
    const int yearlySecondsOnEarth = 31557600;

    readonly int seconds;

    public SpaceAge(int seconds) => 
        this.seconds = seconds;

    public double OnEarth() => this.CalculateYears(orbitalPeriodEarth);

    public double OnMercury() => this.CalculateYears(orbitalPeriodMercury);

    public double OnVenus() => this.CalculateYears(orbitalPeriodVenus);

    public double OnMars() => this.CalculateYears(orbitalPeriodMars);

    public double OnJupiter() => this.CalculateYears(orbitalPeriodJupiter);

    public double OnSaturn() => this.CalculateYears(orbitalPeriodSaturn);

    public double OnUranus() => this.CalculateYears(orbitalPeriodUranus);

    public double OnNeptune() => this.CalculateYears(orbitalPeriodNeptune);

    private double CalculateOrbitalPeriodToSeconds(double orbitalPeriod) =>
        orbitalPeriod * yearlySecondsOnEarth;

    private double CalculateYears(double orbitalPeriod)
    {
        var planetarySeconds = this.CalculateOrbitalPeriodToSeconds(orbitalPeriod);

        return Math.Round(this.seconds / planetarySeconds, 2);
    }
}