# TODO: Feature 3
from src.repositories.movie_repository import get_movie_repository


def test_get_title():
    movie_repository = get_movie_repository()
    movie_repository.clear_db()
    #create movie object
    newMovie = movie_repository.create_movie('Pulp Fiction', 'Tarintino', 5)
    newMovieTitle=newMovie.title
    #getting the newly crated movie by its title
    getMovie = movie_repository.get_movie_by_title(newMovieTitle)

    #compare newmovies.title == thesamemovie but getting it by its title
    assert newMovie.title == getMovie.title

    #check if its not found it should == none
    getMovie = movie_repository.get_movie_by_title('The Matrix')
    assert  getMovie == None