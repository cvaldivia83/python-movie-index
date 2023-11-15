from view import View
from movie import Movie
from import_service import Importer
from export_service import Exporter

class Controller:
    def __init__(self, database):
        self.database = database
        self.view = View()

    def __str__(self):
        return 'CONTROLLER: Movie Controller'

    def list(self):
        movies = self.database.all()
        self.view.list_all_movies(movies)

    def add_movie(self):
        title = self.view.ask_user_for_stuff("title")
        description = self.view.ask_user_for_stuff("description")
        rating = self.view.ask_user_for_stuff("rating")
        seen = self.view.ask_is_movie_seen()
        new_movie = Movie(title, description, rating, seen)
        self.database.create(new_movie)

    def delete_movie(self):
        self.list()
        index = self.view.ask_for_index()
        self.database.destroy(index)

    def mark_as_seen(self):
        self.list()
        index = self.view.ask_for_index()
        movie = self.database.find(index)
        movie.seen = True
        self.database.save_csv()

    def rate_movie(self):
        self.list()
        index = self.view.rate_movie()
        rating = self.view.movie_rating()
        movie = self.database.find(index)
        movie.rating = rating
        self.database.save_csv()

    def find_movie_online(self):
        keyword = self.view.look_for_movie()
        importer = Importer(keyword)
        movie = importer.fetch_movie()
        if isinstance(movie, list):
            answer = self.view.display_imported_movie(movie)
            if answer:
                movie = Movie(movie[0], movie[1])
                self.database.create(movie)
        else:
            print('The requested movie was not found. Please try again with a valid title. \n')


    def export_list(self):
        username = self.view.ask_user_name()
        movies = self.database.movies
        exporter = Exporter(movies, username)
        exporter.export_pdf()


        print("PDF generated in this folder.\n")
        print(f"Your file is named: {username.lower()}_movie_index.pdf")
