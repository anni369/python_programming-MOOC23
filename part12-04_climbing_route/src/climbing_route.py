class ClimbingRoute:
    def __init__(self, name: str, length: int, grade: str):
        self.name = name
        self.length = length
        self.grade = grade
    def __str__(self):
        return f"{self.name}, length {self.length} metres, grade {self.grade}"
    
def sort_by_length(routes: list):
        def by_length(i):
             return i.length
        return sorted(routes, key = by_length, reverse=True)

def sort_by_difficulty(routes: list):
    def by_grade(i):
         return i.grade, i.length
    return sorted(routes, key = by_grade, reverse=True)

     

if __name__ == "__main__":
    r1 = ClimbingRoute("Small steps", 13, "6A+")
    r2 = ClimbingRoute("Edge", 38, "6A+")
    r3 = ClimbingRoute("Bukowski", 9, "6A+")
    reply = sort_by_difficulty([r1, r2, r3])