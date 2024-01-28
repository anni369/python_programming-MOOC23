class LunchCard:
    def __init__(self, balance: float) -> float:
        self.balance = balance

    def deposit_money(self,amount1):
        self.amount += amount1
    def eat_lunch(self):
        if self.balance >= 2.60:
            self.balance -= 2.60
        else:
            pass
    
    def eat_special(self):
        if self.balance >= 4.6:
            self.balance -= 4.60
        else:
            pass

    def __str__(self) -> str:
        return f"The balance is {float(self.balance)} euros"
    
    def deposit_money(self, deposit: float):  
        if deposit < 0:
            raise ValueError ("You cannot deposit an amount of money less than zero")
        else:
            self.balance += deposit
                
if __name__ == "__main__":
    card = LunchCard(10)
    peters_card = LunchCard(20)
    graces_card = LunchCard(30)
    print(card)

    card.eat_lunch()
    print(card)

    card.eat_special()
    card.eat_lunch()
    card.deposit_money(-10)
    print(card)
    card.deposit_money(15)
    print(card)
    card.deposit_money(10)
    print(card)
    card.deposit_money(200)
    print(card)
