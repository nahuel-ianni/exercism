class SpaceAge:
    def __init__(self, seconds):
        self.seconds = seconds
    

    def round(self, number):
        return round(number, 2)


    def on_earth(self):
        return self.round(self.seconds / 31557600)


    def on_mercury(self):
        localSecondsPerYear = 0.2408467 * 31557600
        
        return self.round(self.seconds / localSecondsPerYear)


    def on_venus(self):
        localSecondsPerYear = 0.61519726 * 31557600

        return self.round(self.seconds / localSecondsPerYear)


    def on_mars(self):
        localSecondsPerYear = 1.8808158 * 31557600

        return self.round(self.seconds / localSecondsPerYear)


    def on_jupiter(self):
        localSecondsPerYear = 11.862615 * 31557600

        return self.round(self.seconds / localSecondsPerYear)


    def on_saturn(self):
        localSecondsPerYear = 29.447498 * 31557600

        return self.round(self.seconds / localSecondsPerYear)


    def on_uranus(self):
        localSecondsPerYear = 84.016846 * 31557600

        return self.round(self.seconds / localSecondsPerYear)


    def on_neptune(self):
        localSecondsPerYear = 164.79132 * 31557600

        return self.round(self.seconds / localSecondsPerYear)
