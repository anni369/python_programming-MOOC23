class LunchCard:
    def __init__(self, balance: float):
        self.balance = balance

    def deposit_money(self, amount: float):
        self.balance += amount

    def subtract_from_balance(self, amount: float):
        if amount <= self.balance:
             self.balance -= amount
             return True
        else:
             return False
        
class PaymentTerminal:
    def __init__(self):
        # Initially there is 1000 euros in cash available at the terminal
        self.funds = 1000
        self.lunches = 0
        self.specials = 0

    def eat_lunch(self, payment: float):
        lunch = float (2.50) # A regular lunch costs 2.50 euros.
        if payment >= lunch:
            self.funds += lunch # Increase the value of the funds at the terminal by the price of the lunch,
            self.lunches += 1 # increase the number of lunches sold, and return the appropriate change.
            payment -= lunch # If the payment passed as an argument is not large enough to cover the price,
        return payment # the lunch is not sold, and the entire sum is returned.

    def eat_special(self, payment: float):
        lunch_sp =  float(4.3) # A special lunch costs 4.30 euros.
        if payment >= lunch_sp:
            self.funds += lunch_sp # Increase the value of the funds at the terminal by the price of the lunch,
            self.specials += 1 # increase the number of specials sold, and return the appropriate change.
            payment -= lunch_sp # If the payment passed as an argument is not large enough to cover the price,
        return payment # the lunch is not sold, and the entire sum is returned.
        
    def eat_lunch_lunchcard(self, card: LunchCard):
        luch_reg = float(2.50) # A regular lunch costs 2.50 euros.
        if card.balance >= luch_reg:# If there is enough money on the card, subtract the price of the lunch from the balance
            card.balance -= luch_reg # and return True. If not, return False.
            self.lunches += 1
            return True
        else:
            return False

    def eat_special_lunchcard(self, card: LunchCard):
        lunch_sp = float(4.30) # A special lunch costs 4.30 euros.
        if card.balance >= lunch_sp:# If there is enough money on the card, subtract the price of the lunch from the balance
            card.balance -= lunch_sp # and return True. If not, return False.
            self.specials += 1
            return True
        else:
            return False

    def deposit_money_on_card(self, card: LunchCard, amount: float):
        card.balance += amount

if __name__ == "__main__":
    exactum = PaymentTerminal()

    card = LunchCard(2)
    print(f"Card balance is {card.balance} euros")

    result = exactum.eat_special_lunchcard(card)
    print("Payment successful:", result)

    exactum.deposit_money_on_card(card, 100)
    print(f"Card balance is {card.balance} euros")

    result = exactum.eat_special_lunchcard(card)
    print("Payment successful:", result)
    print(f"Card balance is {card.balance} euros")

    print("Funds available at the terminal:", exactum.funds)
    print("Regular lunches sold:", exactum.lunches)
    print("Special lunches sold:", exactum.specials)