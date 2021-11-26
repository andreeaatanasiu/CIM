"""
Here the program will be started
"""
from functionalities.functions import Functions
from repositories.TextFileRepository import MovieRepositoryFile, ClientRepositoryFile, RentalRepositoryFile, \
    MovieRepositoryPickle, ClientRepositoryPickle, RentalRepositoryPickle
from repositories.repository import MovieRepository, ClientRepository, RentalRepository
from ui.ui import UI
with open("settings.properties", "r") as f:
    mode = f.readline()
    mode = mode.split()
    mode = mode[2]

    if mode == "memory":
        movie_repository = MovieRepository()
        client_repository = ClientRepository()
        rental_repository = RentalRepository()

    elif mode == "text":
        movie_file = f.readline()
        movie_file = movie_file.split()
        movie_file = movie_file[2].strip("\"")
        movie_repository = MovieRepositoryFile(movie_file)

        client_file = f.readline()
        client_file = client_file.split()
        client_file = client_file[2].strip("\"")
        client_repository = ClientRepositoryFile(client_file)

        rental_file = f.readline()
        rental_file = rental_file.split()
        rental_file = rental_file[2].strip("\"")
        rental_repository = RentalRepositoryFile(rental_file)

    elif mode == "binary":
        movie_file = f.readline()
        movie_file = movie_file.split()
        movie_file = movie_file[2].strip("\"")
        movie_repository = MovieRepositoryPickle(movie_file)

        client_file = f.readline()
        client_file = client_file.split()
        client_file = client_file[2].strip("\"")
        client_repository = ClientRepositoryPickle(client_file)

        rental_file = f.readline()
        rental_file = rental_file.split()
        rental_file = rental_file[2].strip("\"")
        rental_repository = RentalRepositoryPickle(rental_file)

    else:
        raise ValueError("Selected mode not valid!")


functions = Functions(movie_repository, client_repository, rental_repository)
ui = UI(functions)
ui.start()
