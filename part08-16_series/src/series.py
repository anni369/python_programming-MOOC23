class Series:
    def __init__(self, title: str, num_of_seasons: int, genres: list) -> None:
        self.title = title
        self.num_of_seasons = num_of_seasons
        self.genres = genres
        self.rate_count = 0
        self.average_rate = 0
        self.rating = 0
    def __str__(self) -> str:
        genres_str = ", ".join(self.genres)
        if self.rating > 0:
            return f"{self.title} ({self.num_of_seasons} seasons)\ngenres: {genres_str}\n{self.rate_count} ratings, average {self.average_rate} points"
        else:
            return f"{self.title} ({self.num_of_seasons} seasons)\ngenres: {genres_str}\nno ratings"

    def rate(self, rating: int):
        self.rate_count += 1
        self.rating += rating
        self.average_rate = self.rating / self.rate_count

    def minimum_grade(self, rating: float, series_list: list):
        for series in series_list:
            if self.rating < rating:
                pass
            return series
            

    def includes_genre(self, genre: str, series_list: list):
        pass


s1 = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
s1.rate(5)
s2 = Series("South Park", 24, ["Animation", "Comedy"])
s2.rate(3)
s3 = Series("Friends", 10, ["Romance", "Comedy"])
s3.rate(2)

series_list = [s1, s2, s3]

print("a minimum grade of 4.5:")
for series in minimum_grade(4.5, series_list):
    print(series.title)

print("genre Comedy:")
for series in includes_genre("Comedy", series_list):
    print(series.title)