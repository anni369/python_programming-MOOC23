class ShoppingList:
    def __init__(self):
        self.products = []

    def number_of_items(self):
        return len(self.products)

    def add(self, product: str, number: int):
        self.products.append((product, number))

    def item(self, n: int):
        return self.products[n - 1][0]

    def amount(self, n: int):
        return self.products[n - 1][1]
# -------------------------
def total_units(my_list: ShoppingList):
    summ =0
    for e in range(0, my_list.number_of_items()):
        summ += my_list.amount(e)
    return summ

if __name__ == "__main__":
    my_list = ShoppingList()
    my_list.add("bananas", 10)
    my_list.add("apples", 5)
    my_list.add("pineapple", 1)


    print(my_list.number_of_items())
    print(my_list.item(1))
    print(my_list.amount(1))
    print(my_list.item(2))
    print(my_list.amount(2))

 

    print(total_units(my_list))