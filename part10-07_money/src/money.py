class Money:
    def __init__(self, euros: int, cents: int):
        self.__euros = euros
        self.__cents = cents

    @property
    def euros(self):
        return self.__euros
    @euros.setter
    def euros(self, euros):
        self.__euros = euros

    @property
    def cents(self):
        return self.__cents
    @cents.setter
    def cents(self, cents):
        self.__cents = cents
        
    def __str__(self):
        return f"{self.__euros}.{self.__cents:02d} eur"
    
    def __eq__(self, another):
        return self.__euros == another.euros and self.__cents == another.cents
    def __lt__(self, another):
        return self.__euros < another.euros or self.__euros == another.euros and self.__cents < another.cents
    def __gt__(self, another):
        return self.__euros > another.euros or self.__euros == another.euros and self.__cents > another.cents
    def __ne__(self, another):
        return self.__euros != another.euros or self.__euros == another.euros and self.__cents != another.cents
    def __add__(self, another):
        new_money = Money(self.__euros, self.__cents)
        new_money.euros = self.__euros + another.euros
        if self.__cents + another.cents < 100:
            new_money.cents = self.__cents + another.cents
        else: 
            new_money.cents = (self.__cents + another.cents) -100
            new_money.__euros +=1
        if new_money.euros < 0:
            raise ValueError("a negative result is not allowed")
        else:
            return new_money      
    def __sub__(self, another):
        new_money = Money(self.__euros, self.__cents)
        new_money.euros = self.__euros - another.__euros
        if self.__cents - another.__cents < 0:
            new_money.cents = (self.__cents - another.__cents)+100
            new_money.euros -=1
        else:
            new_money.cents = self.__cents - another.__cents
        if new_money.euros >= 0:
            return new_money
        else:
            raise ValueError("a negative result is not allowed")
         
if __name__ == "__main__":
    e1 = Money(4, 5)
    print(e1)
    e1.euros = 1000
    print(e1)