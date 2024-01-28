from functools import reduce

class CourseAttempt:
    def __init__(self, course_name: str, grade: int, credits: int):
        self.course_name = course_name
        self.grade = grade
        self.credits = credits

    def __str__(self):
        return f"{self.course_name} ({self.credits} cr) grade {self.grade}"

def sum_of_all_credits(list_attempt: list):
    return reduce(lambda sumoutput, cerdit: sumoutput + cerdit.credits, list_attempt, 0)
def sum_of_passed_credits(list_attempt: list):
    passed = list(filter(lambda l: l.grade > 0, list_attempt))
    return reduce(lambda sumoutput, cerdit: sumoutput + cerdit.credits, passed, 0)
def average(list_attempt: list):
    passed = list(filter(lambda l: l.grade > 0, list_attempt))
    
    return reduce(lambda result, a: (result + a.grade), passed, 0) / len(passed)

if __name__ == "__main__":
    s1 = CourseAttempt("Introduction to Programming", 5, 5)
    s2 = CourseAttempt("Advanced Course in Programming", 0, 4)
    s3 = CourseAttempt("Data Structures and Algorithms", 3, 10)
    ag = average([s1, s2, s3])
    print(ag)