class City:
    country_codes = {"Helsinki": "00100", "Turku": "20100", "Tampere": "33100"}
    def __init__(self, name: str, population: int):
        self.__name = name
        self.__population = population

    @property
    def name(self):
        return self.__name

    @property
    def population(self):
        return self.__population
    
    def postcodes(self):
        return City.country_codes

    def __str__(self):
        return f"{self.__name} ({self.__population} residents.)"
    
if __name__ == "__main__":
    construct = City("Helsinki", 500000)
    print(construct)