import csv
from movie import Movie

class Database:
    def __init__(self, csv_file_path):
        self.csv_file = csv_file_path
        self.movies = []
        self.load_csv()

    def __str__(self):
        return 'DATABASE: MovieIndex DB'

    def all(self):
        return self.movies

    def find(self, index):
        return self.movies[index]

    def create(self, movie):
        self.movies.append(movie)
        self.save_csv()

    def destroy(self, movie_index):
        del self.movies[movie_index]
        self.save_csv()

    def save_csv(self):
        with open(self.csv_file, 'w') as file:
            writer = csv.DictWriter(file, fieldnames=["title", 'description', 'rating', 'seen'])
            writer.writeheader()
            for movie in self.movies:
                writer.writerow({"title": movie.title, "description": movie.description, "rating": movie.rating,
                "seen": movie.seen})


    def load_csv(self):
        with open(self.csv_file) as file:
            reader = csv.DictReader(file)
            for row in reader:
                row["seen"] = row["seen"] == 'True'
                movie = Movie(row["title"], row["description"], int(row["rating"]), row["seen"])
                self.movies.append(movie)
