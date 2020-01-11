class BankAccount:
    def __init__(self):
        self._reset()


    def get_balance(self):
        self._guard_closed_account()

        return self.balance


    def open(self):
        if self.active:
            raise ValueError("Unsupported operation: Opened account")

        self.active = True


    def deposit(self, amount):
        self._guard_closed_account()
        self._guard_negative_amount(amount)

        self.balance += amount
        

    def withdraw(self, amount):
        self._guard_closed_account()
        self._guard_negative_amount(amount)

        if self.balance < amount:
            raise ValueError("Unsupported operation: Insufficient funds")

        self.balance -= amount


    def close(self):
        self._guard_closed_account()

        self._reset()

    
    def _guard_closed_account(self):
        if not self.active:
            raise ValueError("Unsupported operation: Closed account")

    
    def _guard_negative_amount(self, amount):
        if amount < 0:
            raise ValueError("Unsupported operation: Negative amount")


    def _reset(self):
        self.active = False
        self.balance = 0
