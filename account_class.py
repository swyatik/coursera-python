class Value:
    _val = 0
    def __get__(self, instance, owner):
        return self._val

    def __set__(self, instance, value):
        self._val = round(value - value * instance.commission)


class Account:
    amount = Value()

    def __init__(self, commission):
        self.commission = commission



new = Account(0.1)
print('new.commission: {} new.amount: {}'.format(new.commission, new.amount))

new.amount = 900
print('new.commission: {} new.amount: {}'.format(new.commission, new.amount))


