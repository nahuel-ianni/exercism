class Luhn:
    def __init__(self, card_num):
        self.card = card_num.replace(" ", "")

    def valid(self):
        if not (self.card.isdigit() and len(self.card) > 1):
            return False

        digits = list(reversed([int(x) for x in self.card if x.isdigit()]))

        for i in range(1, len(digits), 2):
            num = digits[i] * 2
            digits[i] = num if num < 10 else num - 9

        return sum(digits) % 10 == 0
