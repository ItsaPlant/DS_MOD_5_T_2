import random
from datetime import datetime


class MopicLibrary:
    def __init__(self):
        self.library = []

    def add_mopic(self, mopic):
        self.library.append(mopic)

    def generate_views(self):
        for _ in range(10):
            mopic = random.choice(self.library)
            mopic.play()

    def display_top_titles(self, count, content_type=None):
        sorted_library = sorted(self.library, key=lambda mopic: mopic.views, reverse=True)
        if content_type == 'movies':
            movies = [m for m in sorted_library if isinstance(m, Movie)]
            return movies[:count]
        elif content_type == 'series':
            series = [s for s in sorted_library if isinstance(s, Series)]
            return series[:count]
        else:
            return sorted_library[:count]

    def display_library(self):
        for mopic in self.library:
            print(mopic)

    def display_available_episodes(self, series_title):
        available_episodes = sum(1 for mopic in self.library if isinstance(mopic, Series) and mopic.title == series_title)
        print(f"Available episodes of {series_title}: {available_episodes}")


class Mopic:
    def __init__(self, title, year, genre):
        self.title = title
        self.year = year
        self.genre = genre
        self.views = 0

    def play(self):
        self.views += 1

    def __str__(self):
        return f'{self.title}'

    def __repr__(self):
        return f'{self.title}'


class Series(Mopic):
    def __init__(self, title, year, genre, season, episode):
        super().__init__(title, year, genre)
        self.season = season
        self.episode = episode

    def __str__(self):
        return f'{self.title} S{self.season:02}E{self.episode:02}'


class Movie(Mopic):
    def __init__(self, title, year, genre):
        super().__init__(title, year, genre)

    def __str__(self):
        return f'{self.title} ({self.year})'


def generate_sample_library():
    library = MopicLibrary()

    for _ in range(5):
        movie = Movie(f'Movie{_}', random.randint(1990, 2022), 'Action')
        library.add_mopic(movie)

    for _ in range(5):
        series = Series(f'Series{_}', random.randint(1990, 2022), 'Drama', random.randint(1, 10), random.randint(1, 20))
        library.add_mopic(series)

    return library


if __name__ == "__main__":
    print('Biblioteka filmów')
    
    mopic_library = generate_sample_library()
    
    # Display the library
    mopic_library.display_library()
    
    # Generate views
    mopic_library.generate_views()
    
    # Display top titles
    top_titles = mopic_library.display_top_titles(3)
    print("\nTop 3 Titles:")
    for title in top_titles:
        print(title)
    
    # Display available episodes for a series
    series_title_to_check = "Series0"
    mopic_library.display_available_episodes(series_title_to_check)
