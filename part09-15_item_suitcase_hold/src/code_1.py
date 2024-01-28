class Item:
    def __init__(self, name: str, weight: int) -> None:
        self.__name = name
        self.__weight = weight
    def name(self):
        return self.__name
    def weight(self):
        return self.__weight
    def __str__(self) -> str:
        return f"{self.__name} ({self.__weight} kg)"
    
class Suitcase:
    def __init__(self, s_weight: int) -> None:
        self.s_weight = s_weight
        self.suitcase = []
        self.sum_weight = 0
    def add_item(self, item: Item):
        if item.weight() + self.sum_weight <= self.s_weight:
            self.suitcase.append(item)
            self.sum_weight += item.weight()
        else:
            pass

    def print_items(self):
        for e in self.suitcase:
            print(e)

    def weight(self):
        return self.sum_weight
    
    def heaviest_item(self):
        if self.suitcase != []:
            index_maxweight = []
            for e in self.suitcase:
                index_maxweight.append(e.weight())
            maxindex = index_maxweight.index(max(index_maxweight))
            return self.suitcase[maxindex]
        else:
            return None

    def __str__(self) -> str:
        if len(self.suitcase) ==1:
            return f"{len(self.suitcase)} item ({self.sum_weight} kg)"
        else:
            return f"{len(self.suitcase)} items ({self.sum_weight} kg)"

class CargoHold:
    def __init__(self, maxweight: int) -> None:
        self.maxweight = maxweight
        self.ammount = 0
        self.items_weight = 0
        self.cargolist = []
    def add_suitcase(self, suitcase: Suitcase):
        if self.maxweight >= self.items_weight + suitcase.weight():
            self.ammount +=1
            self.items_weight += suitcase.weight()
            self.maxweight -= suitcase.weight()
            self.cargolist.append(suitcase)
        else:
            pass

    def print_items(self):
        for item in self.cargolist:
            print(item)

    def __str__(self) -> str:
        return f"{self.ammount} suitcases, space for {self.maxweight} kg"


if __name__ == "__main__":
    book = Item("ABC Book", 2)
    phone = Item("Nokia 3210", 1)
    brick = Item("Brick", 4)

    suitcase = Suitcase(10)
    suitcase.add_item(book)
    suitcase.add_item(phone)
    suitcase.add_item(brick)

    heaviest = suitcase.heaviest_item()
    print(f"The heaviest item: {heaviest}")
