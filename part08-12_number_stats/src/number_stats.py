class  NumberStats:
    def __init__(self):
        self.numbers = []
        self.evens = []
        self.odds = []

    def add_number(self, number:int):
        self.numbers.append(number)
        if number / 2 == 0:
            self.evens.append(number)
        elif number / 2 != 0:
            self.odds.append(number)
        pass

    def count_numbers(self):
        count = len(self.numbers)
        return count

    def get_sum(self):
        if self.numbers != []:
            summe = sum(self.numbers)
        else:
            summe = 0
        return summe
             
    def average (self):
        if self.numbers != []:
            ave = self.get_sum()/self.count_numbers()
        else:
            ave = 0
        return ave

stats = NumberStats()

while True:
    inp = int(input("Please type in integer numbers:"))
    if inp == -1:
        print("Sum of numbers:", stats.get_sum())
        print("Mean of numbers:", stats.average())
        print("Sum of even numbers: ", stats.average())
        print("Sum of odd numbers: ", stats.average())
        break
    else:
        stats.add_number(inp)
    

