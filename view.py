class View:
    def __str__(self):
        return "VIEW: User Interface"

    def ask_user_name(self):
        print('What is your name?\n')
        return input('Name: ')

    def ask_user_for_stuff(self, stuff):
        return input(f"What is the {stuff} of this movie?")

    def ask_is_movie_seen(self):
        answer = input("Have you already seen this movie? [Y/N]")
        return answer.capitalize() == 'Y'

    def rate_movie(self):
        return (int(input("Which movie would you like to rate?")) - 1)

    def movie_rating(self):
        print("Which rating would you like to give? \n")
        return int(input("Rating [1 - 5]:"))

    def ask_for_index(self):
        print("Which movie would you like to select? \n")
        return (int(input("Index: ")) - 1)

    def look_for_movie(self):
        print("How is the movie you're searching for called? \n")
        return input('Type a valid title: ')

    def display_imported_movie(self, list):
        print(f"{list[0]} \n")
        print(f"{list[1]} \n")
        print("Would you like to save this movie in your list?")
        answer = input("Confirm [Y/N]: ")
        return answer == 'Y'

    def list_all_movies(self, movies):
        for index, movie in enumerate(movies):
            print(f"{index + 1} - {'[X]' if movie.seen else '[ ]'} - {movie.title} - {movie.rating}/5 \n => {movie.description} \n")
