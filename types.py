import random
import datetime # from datetime import datetime
from faker import Faker
from faker.providers import DynamicProvider

fake = Faker()

genres_provider = DynamicProvider(
    provider_name="genre",
    elements=['nudny', 'chwytający za serce', 'Netflix not-so-originial', 'jeden na milion', 'nie skończysz i tak', 'nawet nie zaczynaj']
)

fake = Faker()
fake.add_provider(genres_provider)


mopic_list = []
class Mopic:
    def __init__(self, title, release, genre, views):
        self.title = title
        self.release = release
        self.genre = genre
        self.views = views
    
    def __str__(self):
        return f'{self.title}'


    def __repr__(self):
        return f'{self.title}'

    
    def play(self):
        self.views + 1


    def generate_views():
        for i in range(random.randint(0, 100)):
            mopic.play()

    
    @staticmethod
    def getmovies(mopic_list):
        movies = []
        for mopic in mopic_list:
            if isinstance(mopic, Movie):
                movies.append(mopic)
        return movies
    

    @staticmethod
    def getseries(mopic_list):
        series = []
        for mopic in mopic_list:
            if isinstance(mopic, Series):
                series.append(mopic)
        return series
    

    @staticmethod
    def search(mopic_list, name):
        for mopic in mopic_list:
            if mopic.name == name:
                return mopic
            else:
                return 'NOT FOUND'
    

    @staticmethod
    def top_titles(mopic_list, count, content_type=None):
        if content_type == 'M':
            mopic_list = Mopic.getmovies(mopic_list)
        elif content_type == 'S':
            mopic_list = Mopic.getseries(mopic_list)
        return mopic_list.sort(key=lambda mopic: mopic.views, reverse=True)[0:count]


class Series(Mopic):
    def __init__(self, no_season, no_epizode, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._no_season = no_season
        self._no_epizode = no_epizode
    

    def __str__(self):
        return f'{self.title}, S{self._no_season:02d}E{self._no_epizode:02d}'
    

    @property
    def get_season_number(self):
        return f"{self._no_season:02d}"
    

    @property
    def get_epizode_number(self):
        return f"{self._no_epizode:02d}"
    

    def generate():
        pass
    

class Movie(Mopic):
    def __str__(self):
        return f'{self.title}, {self.release}'
    

    def generate():
        pass

def generate():
    title = fake.name()
    release = random.randint(1900, 2050)
    genre = fake.genre()
    views = random.randint(0, 50000)
    no_season = random.randint(1, 99)
    no_epizode = random.randint(1, 99)
    return (title, release, genre, views, no_season, no_epizode)


if __name__ == "__main__":
    
    count_movies = random.randint(3, 6)
    count_series = random.randint(8, 12)

    title, release, genre, views, no_season, no_epizode = generate()

    for i in range(count_movies):
        movie = Movie(title, release, genre, views, no_season)
        mopic_list.append(movie)
    for i in range(count_series):
        series = Series(title, release, genre, views, no_season, no_epizode)
        mopic_list.append(series)
    for mopic in mopic_list:
        mopic.generate_views()
    print('Mopic Library')
    top_3 = Mopic.top_titles(mopic_list=mopic_list, count=3)
    dtnow = datetime.today().strftime('%Y-%m-%d')
    print(f'Najpopularniejsze filmy i seriale z dnia {dtnow}:')
    for top in top_3:
        print(top)
    

