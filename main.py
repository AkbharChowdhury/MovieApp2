from tkinter import *
from tkinter import ttk

from classes.db import Database
from classes.models.movie import Movie

db = Database()


class MovieList:
    @staticmethod
    def calc_duration(minutes=90):
        h = minutes // 60
        m = minutes % 60
        return f'{h}:{m}'

    def __init__(self, master):
        self.master = master
        self.master.title("Movie List")
        self.master.geometry("900x950")

        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.style.configure('Treeview', rowheight=46)

        self.columns = Movie.columns()
        self.col_length = tuple([f"c{i}" for i, column in enumerate(self.columns, start=1)])

        self.tree = ttk.Treeview(self.master, column=self.col_length, show='headings', height=5)
        for i, column in enumerate(self.columns, start=1):
            self.tree.column(f"# {i}", anchor=CENTER)
            self.tree.heading(f"# {i}", text=column)

        movie_data = Movie.get_movie_data()
        # for i in movie_data:
        #     data = movie_data.get(i)
        #     lst = [data.get('title'), MovieList.calc_duration(int(data.get('duration'))), data.get('rating'),
        #            '/'.join(data.get('genres'))]
        #     print(lst)
        #     # display
        #     self.tree.insert('', 'end', text="1", values=lst)

        # for movie in movie_data:
        #     self.tree.insert('', 'end', text="1", values=movie)
        print(Movie.getMovieList(db.movie_list()))
        for m in Movie.getMovieList(db.movie_list()):
            self.tree.insert('', 'end', text="1", values=[m.title, m.duration, m.rating, '/'.join(m.genres)])
        self.tree.pack()


def main():
    import tkinter as tk

    root = tk.Tk()
    MovieList(root)
    root.resizable()
    root.mainloop()


if __name__ == '__main__':
    main()
    # my_list = Movie.getMovieList(db.movie_list())
    # for m in my_list:
    #     print(m)
    # s = input("Title").lower()
    #
    # l = [x for x in my_list if s in x.title.lower()]
    # for movie in l:
    #    print(movie)


    # print(db.movie_list())
    # data = db.movie_list()
    # data = Movie.getMovieList(data)
    # print(type(data))
    # for movie in data:
    #     print(movie.title, sep=' ')
