import requests


class Importer:
    def __init__(self, keyword):
        self.keyword = keyword

    def __str__(self):
        return 'IMPORTER - Movie import'

    def fetch_movie(self):
        url = f'http://www.omdbapi.com/?t={self.keyword}&apikey=c21805ae'
        response = requests.get(url)
        result = response.json()
        if 'Title' in result:
            return [result["Title"], result["Plot"]]
        else:
            return result['Error']
