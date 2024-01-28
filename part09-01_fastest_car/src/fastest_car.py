# Write your solution after the class Car
# Do not make changes to the class 
class Car:
    def __init__(self, make: str, top_speed: int):
        self.make = make
        self.top_speed = top_speed
   
    def __str__(self):
        return f"Car (make: {self.make}, top speed: {self.top_speed})"

"""def fastest_car(cars: list):
    max_speed = []
    car_marke = []
    for car in cars:
        max_speed.append(car.top_speed)
        car_marke.append(car.make)
    i = max_speed.index(max(max_speed))
    name = car_marke[i]
    return name"""
def fastest_car(cars: list):
    fastest_make = cars[0].make
    best_speed = cars[0].top_speed
 
    for car in cars:
        if car.top_speed > best_speed:
            best_speed = car.top_speed
            fastest_make = car.make
 
    return fastest_make
    

     
# WRITE YOUR SOLUTION HERE:
if __name__ == "__main__":
    car1 = Car("Saab", 195)
    car2 = Car("Lada", 110)
    car3 = Car("Ferrari", 280)
    car4 = Car("Trabant", 85)

    cars = [car1, car2, car3, car4]
    print(fastest_car(cars))