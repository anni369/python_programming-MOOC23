class BankAccount:
    def __init__(self, owner: str, number: str, balance: float ) -> None:
        self.__owner = owner
        self.__number = number
        self.__balance = balance

    def deposit(self, amount: float):
        self.balance += amount
        self.__service_charge()
        
    def withdraw(self, amount: float):
        self.balance -= amount
        self.__service_charge()
    
    @property
    def balance(self):
        return self.__balance
    @balance.setter
    def balance(self, balance):
        self.__balance = balance
    
    def __service_charge(self):
        self.balance *= 0.99

        


if __name__ == "__main__":
    account = BankAccount("Randy Riches", "12345-6789", 1000)
    account.withdraw(100)
    print(account.balance)
    account.deposit(100)
    print(account.balance)

