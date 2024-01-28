class SimpleDate:
    def __init__(self, dd:int, mm:int, yy: int) -> None:
        self.dd = dd
        self.mm = mm
        self.yy = yy
    def __str__(self) -> str:
        return f"{self.dd}.{self.mm}.{self.yy}"
    
    def value(self):
        return self.yy * 360 + self.mm * 30 + self.dd
    def back_to_date(self, days: int):
        dd = days % 30
        mm = (days // 30) % 12
        yy = (days // 30) // 12
        return SimpleDate(dd, mm, yy)
    
    def __eq__(self, another: "SimpleDate") -> bool:
        return self.value() == another.value()
    def __ne__(self, another: "SimpleDate") -> bool:
        return self.value() != another.value()   
    def __lt__(self, another: "SimpleDate"): 
            return self.value() < another.value()
    def __gt__(self, another: "SimpleDate"):
            return self.value() > another.value()    
    def __add__(self, days_input: int):
        return self.back_to_date(self.value() + days_input) 
    def __sub__(self, another:"SimpleDate"):
        return abs(self.value() - another.value())
        
if __name__ == "__main__":
    d1 = SimpleDate(4, 10, 2020)
    d2 = SimpleDate(28, 12, 1985)
    d3 = d1 + 3
    d4 = d2 + 400
    print(d1)
    print(d2)
    print(d3)
    print(d4)

