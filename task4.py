class BankAccount:
    def __init__(self, initial_balance=0):
        self._balance = initial_balance
        self._transactions = []

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            self._transactions.append(f"Внесено: {amount}")
            print(f"Успешно внесено: {amount}. Текущий баланс: {self._balance}")
        else:
            print("Сумма депозита должна быть положительной.")

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            self._transactions.append(f"Снято: {amount}")
            print(f"Успешно снято: {amount}. Текущий баланс: {self._balance}")
        elif amount > self._balance:
            print("Недостаточно средств для снятия.")
        else:
            print("Сумма снятия должна быть положительной.")

    def get_transactions(self):
        return self._transactions



if __name__ == "__main__":
    account = BankAccount(100)
    account.deposit(50)
    account.withdraw(30)
    account.withdraw(150)
    account.deposit(-20)

    print("\nИстория транзакций:")
    for transaction in account.get_transactions():
        print(transaction)

    print(f"Текущий баланс: {account.balance}")