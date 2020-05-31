class Luhn:
    def __init__(self, card_num):
        self.card = card_num.replace(" ", "")

    def valid(self):
        if not self._guardInput():
            return False

        digits = list(reversed(self._curateInput(self.card)))

        for i in range(1, len(digits), 2):
            digits[i] = self._doubleNumber(digits[i])

        return sum(digits) % 10 == 0

    def _guardInput(self):
        return len(self.card) > 1 and \
            not any(x for x in self.card if not x.isdigit())

    def _curateInput(self, input):
        return [int(x) for x in input if x.isdigit()]

    def _doubleNumber(self, num):
        num = num * 2
        return num if num < 10 else num - 9