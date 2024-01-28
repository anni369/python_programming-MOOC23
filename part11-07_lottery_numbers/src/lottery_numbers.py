class LotteryNumbers:
    def __init__(self, week_number: int, lists: list) -> None:
        self.week_number = week_number
        self.lists = lists
    def number_of_hits(self, numbers: list):
        return len([n for n in numbers if n in self.lists])
    
    def hits_in_place(self, numbers):
        return [n if n in self.lists else -1 for n in numbers]




if __name__ == "__main__":
    week8 = LotteryNumbers(8, [1,2,3,10,20,30,33])
    my_numbers = [1,4,7,10,11,20,30]

    print(week8.hits_in_place(my_numbers))