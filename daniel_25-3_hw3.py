class Bank:
    money = 'money'

    def __init__(self, name, balance=100):
        self._name = name
        self._balance = balance

    def __str__(self):
        return f'{self._name}' \
               f' {self._balance}'

    def moneyX(self):
             amount = int(input('Сколько хотите добвавить на счет?-'))
             self._balance += amount
             print(self._balance)

    def _kill(self):
        self._balance = 0

    def __jackpot(self):
        self._balance *= 10

    def _sss(self, obj):
        return self._balance + obj._balance
a = Bank('Miko')
a.moneyX()
#a._kill()
a._sss(a)
print(a._sss(a))
print(a._name, a._sss(a))




