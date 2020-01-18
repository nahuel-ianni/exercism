class PhoneNumber:
    def __init__(self, number):
        digits = [char for char in number if char.isdecimal()]

        self._guard_number(digits)

        if len(digits) == 11:
            digits = digits[1:]

        self.number = "".join(digits)
        self.area_code = self.number[:3]
        self.exchange_code = self.number[3:6]
        self.subscriber_number = self.number[6:]

        if self.area_code[0] in ['0', '1'] or self.exchange_code[0] in ['0', '1']:
            raise ValueError("Unsupported operation: Area code and exchange code values must range from 2 to 9.")


    def pretty(self):
        return f"({self.area_code}) {self.exchange_code}-{self.subscriber_number}"

    
    def _guard_number(self, digits):
        length = len(digits)

        if length not in [10, 11] or (length == 11 and digits[0] != "1"):
            raise ValueError("Unsupported operation: Phone number length.")
