class ListHelper:
    def __init__(self) -> None:
        pass
    @classmethod
    def greatest_frequency(cls, my_list: list):
        return max(set(my_list), key = my_list.count)
    @classmethod
    def doubles(cls, my_list: list):
        counter = []
        for e in my_list:
            occurance = my_list.count(e)

            if occurance <= 2 and e not in counter:
                counter.append(e)
        print (counter)
        return len(counter)
            


if __name__ == "__main__":
    numbers = [3, 2, 3, 2, 2, 3, 1, 2, 4, 5, 5, 6]
    print(ListHelper.greatest_frequency(numbers))
    print(ListHelper.doubles(numbers))