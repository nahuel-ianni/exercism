from enum import IntEnum


class PlanetarySeconds(IntEnum):
    Earth   = 31557600
    Mercury = 0.2408467  * Earth
    Venus   = 0.61519726 * Earth
    Mars    = 1.8808158  * Earth
    Jupiter = 11.862615  * Earth
    Saturn  = 29.447498  * Earth
    Uranus  = 84.016846  * Earth
    Neptune = 164.79132  * Earth


class SpaceAge:
    def __init__(self, seconds):
        self.seconds = seconds


    def on_earth(self):
        return self.calculate_years(PlanetarySeconds.Earth)


    def on_mercury(self):
        return self.calculate_years(PlanetarySeconds.Mercury)


    def on_venus(self):
         return self.calculate_years(PlanetarySeconds.Venus)


    def on_mars(self):
        return self.calculate_years(PlanetarySeconds.Mars)


    def on_jupiter(self):
        return self.calculate_years(PlanetarySeconds.Jupiter)


    def on_saturn(self):
        return self.calculate_years(PlanetarySeconds.Saturn)


    def on_uranus(self):
        return self.calculate_years(PlanetarySeconds.Uranus)


    def on_neptune(self):
        return self.calculate_years(PlanetarySeconds.Neptune)


    def calculate_years(self, planetary_seconds):        
        return round(self.seconds / planetary_seconds, 2)
