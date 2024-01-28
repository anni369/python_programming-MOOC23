class Recording:
    def __init__(self, length) -> None:
        self.length = length
        
    @property
    def length(self):
        return self.__length
    
    @length.setter
    def length(self, length):
        if length < 0:
            raise ValueError("Length cannot be below zero.")
        self.__length = length
        
if __name__ == "__main__":
    the_wall = Recording(-1)
    print(the_wall.length)
    the_wall.length = 44
    print(the_wall.length)