class Person:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

    def __str__(self):
        return self.name
    
class Room:
    def __init__(self) -> None:
        self.room = []
        self.addperson = 0
        self.addheight = 0

    def add(self, person: Person):
        self.room.append(person)
        self.addperson +=1
        self.addheight += person.height

    def is_empty(self):
        if self.room == []:
            return True
        else:
            return False
        
    def print_contents(self):
        print(f"There are {self.addperson} persons in the room, and their combined height is {self.addheight} cm")
        for pers in self.room:
            print (f'{pers.name} ({pers.height} cm)')

    def shortest(self):
        min_height = []
        if self.room != []:
            for person in self.room:
                min_height.append(person.height)
            min_index = min_height.index(min(min_height))
            return self.room[min_index]
        else:
            return None
        
    def  remove_shortest(self):
        schortest = self.shortest() # Utilizing the previous method
        if schortest:  # equals to conditon shortest person is not None
            self.room.remove(schortest)
            return schortest
        
        
if __name__ == "__main__":
    room = Room()

    room.add(Person("Lea", 183))
    room.add(Person("Kenya", 172))
    room.add(Person("Nina", 162))
    room.add(Person("Ally", 166))
    room.print_contents()

    print()

    removed = room.remove_shortest()
    print(f"Removed from room: {removed.name}")

    print()

    room.print_contents()