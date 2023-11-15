class Movie:
    def __init__(self, title, description, rating=0, seen=False):
        self.title = title
        self.description = description
        self.rating = rating
        self.seen = seen

    def __str__(self):
        return f"MOVIE - title:{self.title} - rating: {self.rating} - seen: {self.seen}"

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        if not title:
            raise TypeError('A movie must have a title.')
        self._title = title

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        if not description:
            raise TypeError('A movie must have a description.')
        self._description = description
