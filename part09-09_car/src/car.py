class Car:
    def __init__(self) -> None:
        self.__petrol = 0
        self.__odometer = 0

    def fill_up(self):
        if self.__petrol >= 0 and self.__petrol < 60:
            self.__petrol = 60
 
    def drive(self, km: int):
        difference = self.__petrol - km
        if difference >= 0:
            self.__petrol -= km
            self.__odometer += km
        else: 
            self.__petrol -= km + difference
            self.__odometer += km + difference
            
    
    def __str__(self) -> str:
        return f"Car: odometer reading {self.__odometer} km, petrol remaining {self.__petrol} litres"
   
if __name__ == "__main__":
    car = Car()
    print(car)
    car.fill_up()
    print(car)
    car.drive(20)
    print(car)
    car.drive(50)
    print(car)
    car.drive(10)
    print(car)
    car.fill_up()
    car.fill_up()
    print(car)