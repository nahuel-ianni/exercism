import re as regex


class PhoneNumber:
    def __init__(self, number):
        self.number = "".join([n for n in number if n.isdecimal()])
        self._guard_length(self.number)
        self._guard_format(self.number)

        self.number = self.number if len(self.number) == 10 else self.number[1:]
        self.area_code = self.number[:3]


    def pretty(self):
        return f"({self.area_code}) {self.number[3:6]}-{self.number[6:]}"


    def _guard_length(self, number):
        if len(number) not in {10, 11} or (len(number) == 11 and number[0] != "1"):
            raise ValueError("Unsupported operation: Phone number length.")
    

    def _guard_format(self, number):
        pattern = "1?\\W*([2-9][0-8][0-9])\\W*([2-9][0-9]{2})\\W*([0-9]{4})(\\se?x?t?(\\d*))?"

        if not regex.findall(pattern, number):
            raise ValueError("Unsupported operation: Phone number length.")
