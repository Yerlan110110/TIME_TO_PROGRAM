class BankAccount:
    def __init__(self, owner, balance):
        self.__owner = owner
        self.__balance = balance
    @property
    def balance(self):
        return self.__balance


    def deposit(self, amount):
        if amount >= 0:
            self.__balance += amount
        else:
            print('Значение меньше нуля!')


    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print('У вас недостаточно средств!')


acc = BankAccount("Сергей", 1000)
print(acc.balance)   # 1000
acc.deposit(500)
print(acc.balance)   # 1500
acc.withdraw(2000)   # Ошибка: недостаточно средств
print(acc.balance)   # 1500
