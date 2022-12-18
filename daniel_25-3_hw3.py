class Bank:
    money = 'money'

    def __init__(self, name, balance=50):
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

    def sss(self, str):
        return self._balance + str._balance

    def _sss(self, str ):
        return self._balance -  str._balance

a = Bank('Beka')
a.name ='Miko'
a.moneyX()
#a._kill()
a._sss(a)
a.sss(a)
print(a.name,a._sss(a))
print(a._name,a.sss(a))




