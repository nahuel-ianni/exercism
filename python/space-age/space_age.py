class SpaceAge:
    def __init__(self, seconds):
        self.seconds = seconds


    def on_earth(self):
        return self.calculate_years(1)


    def on_mercury(self):
        return self.calculate_years(0.2408467)


    def on_venus(self):
         return self.calculate_years(0.61519726)


    def on_mars(self):
        return self.calculate_years(1.8808158)


    def on_jupiter(self):
        return self.calculate_years(11.862615)


    def on_saturn(self):
        return self.calculate_years(29.447498)


    def on_uranus(self):
        return self.calculate_years(84.016846)


    def on_neptune(self):
        return self.calculate_years(164.79132)

    
    def orbital_period_to_seconds(self, orbital_period):
        return orbital_period * 31557600


    def calculate_years(self, orbital_period):
        planetary_seconds = self.orbital_period_to_seconds(orbital_period)
        
        return round(self.seconds / planetary_seconds, 2)
