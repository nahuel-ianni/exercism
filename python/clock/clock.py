class Clock:
    def __init__(self, hour, minute):
        self._minutes = (hour * 60 + minute) % 1440

    def __str__(self):
        hours, minutes = divmod(self._minutes, 60)
        return f'{hours:02d}:{minutes:02d}'

    def __eq__(self, other):
        return str(self) == str(other)

    def __add__(self, minutes):
        return self.__class__(0, self._minutes + minutes)

    def __sub__(self, minutes):
        return self.__class__(0, self._minutes - minutes)
