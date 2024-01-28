class WeatherStation:
    def __init__(self, name) -> None:
        self.__name = name
        self.__my_list = []
    """@property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        
        if name != "":
            self.__name = name
        else:
            raise ValueError("The name may not be an empty string")"""
        
    def add_observation(self, observation: str):
        self.__my_list.append(observation)

    def latest_observation(self):
        if self.__my_list == []:
            return ""
        else:
            return self.__my_list[-1]

    def number_of_observations(self):
        number = len(self.__my_list)
        return number

    def __str__(self) -> str:
        return f"{self.__name}, {len(self.__my_list)} observations"

if __name__ == "__main__":
    station = WeatherStation("Houston")
    station.add_observation("Rain 10mm")
    station.add_observation("Sunny")
    print(station.latest_observation())

    station.add_observation("Thunderstorm")
    print(station.latest_observation())

    print(station.number_of_observations())
    print(station)

