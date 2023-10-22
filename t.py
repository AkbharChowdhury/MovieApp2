# class Movie:
#     def __int__(self, title, duration, rating, genres):
#         self.title = title
#         self.duration = duration
#         self.rating = rating
#         self.genres = genres
from classes.db import Database

db = Database()
from  classes.models.movie import  Movie

# class Movie:
#     def __init__(self, title, duration, rating, genres):
#         self.title = title
#         self.duration = duration
#         self.rating = rating
#         self.genres = genres


movie_data = db.movie_list()
def getMovieList(movie_data):
    # return [Movie(title=row[0], duration=int(row[1]), rating=row[2], genres='/'.join(row[3])) for row in movie_data]
    return [Movie(title=row[0], duration=int(row[1]), rating=row[2], genres=row[3].split('/')) for row in movie_data]

for movie in getMovieList(movie_data):
    print( movie.genres, sep=' ')

print(getMovieList(movie_data))
exit(0)
# creating list
list = []

# appending instances to list

list.append(Movie('Spiderman', 200, '13', ['Action']))
list.append(Movie('Superman', 180, '13', ['Action']))
list.append(Movie("Child's play", 180, '13', ['Horror', 'Thriller']))

# list.append(geeks('Reaper', 44))
# list.append(geeks('veer', 67))

# Accessing object value using a for loop
for movie in list:
    print(movie.title, movie.genres, sep=' ')

# Accessing individual elements
# for i, d in enumerate(list):
#     print(i, d)
# print(list[0].name)
# print(list[1].name)
# print(list[2].name)
# print(list[3].name)
