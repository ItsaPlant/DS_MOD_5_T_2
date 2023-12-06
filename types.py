import random
import datetime # from datetime import datetime

class Mopic:
    def __init__(self):
        self.title = None
        self.release = None
        self.genre = None
        self.views = 0
    
    def __str__(self):
        return f'{self.title}'


    def __repr__(self):
        return f'{self.title}'

    
    def play(self):
        self.views + 1

    
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
    def generate_views(mopic_list):
        for mopic in mopic_list:
            for i in range(random.randint(0, 100)):
                mopic.play()
    

    @staticmethod
    def top_titles(mopic_list, count, content_type=None):
        if content_type == 'M':
            mopic_list = Mopic.getmovies(mopic_list)
        elif content_type == 'S':
            mopic_list = Mopic.getseries(mopic_list)
        return mopic_list.sort(key=lambda mopic: mopic.views, reverse=True)[0:count]


class Series(Mopic):
    def __init__(self):
        super().__init__()
        self.no_season = None
        self.no = None
    

    def __str__(self):
        return f'{self.title}, S{self.no_season}E{self.no}'
    

    def generate():
        pass
    

class Film(Mopic):
    def __str__(self):
        return f'{self.title}, {self.release}'
    

    def generate():
        pass


if __name__ == "__main__":
    print('Mopic Library')
    count_movies = random.randint(3, 6)
    count_series = random.randint(8, 12)

    ##generate data

    top_3 = Mopic.top_titles(mopic_list=mopic_list, count=3)
    dtnow = datetime.today().strftime('%Y-%m-%d')
    

