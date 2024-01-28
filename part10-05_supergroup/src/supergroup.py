class SuperHero:
    def __init__(self, name: str, superpowers: str):
        self.name = name
        self.superpowers = superpowers
    def __str__(self):
        return f'{self.name}, superpowers: {self.superpowers}'
    def __repr__(self) -> str:
        return self.__str__()
    

class SuperGroup:
    def __init__(self, name: str, location: str):
        self._name = name
        self._location = location
        self._members = []
    @property
    def name (self):
        return self._name
    @property
    def location (self):
        return self._location
    @location.setter
    def name(self,name):
        self._name = name
    @location.setter
    def name(self,location):
        self._location = location

    def add_member(self, hero: SuperHero):
        self._members.append(hero)

    def print_group(self):
        print (f'{self._name}, {self._location}\nMembers:')
        for e in self._members:
            print (e)

if __name__ == "__main__":
    superperson = SuperHero("SuperPerson", "Superspeed, superstrength")
    invisible = SuperHero("Invisible Inca", "Invisibility")
    revengers = SuperGroup("Revengers", "Emerald City")
    revengers.add_member(superperson)
    revengers.add_member(invisible)
    revengers.print_group()
