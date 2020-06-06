class Clock:
    def __init__(self, hour, minute):
        self.hours = hour
        self.minutes = minute

    def __repr__(self):
        return f"{self.hours:02d}:{self.minutes:02d}"

    def __eq__(self, other):
        return str(self) == str(other)

    def __add__(self, minutes):
        pass

    def __sub__(self, minutes):
        pass
