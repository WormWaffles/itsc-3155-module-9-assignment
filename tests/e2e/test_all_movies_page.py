# TODO: Feature 1
import pytest
from app import app
from src.repositories.movie_repository import get_movie_repository

def test_all_movies_page():
    test_app = app.test_client()
    response = test_app.get('/movies')
    assert response.status_code == 200
    assert b'<td colspan="3">No movies found</td>' in response.data

def test_show_movie():
    test_app = app.test_client()
    movie_repository = get_movie_repository()
    movie_repository.create_movie('The Matrix', 'Wachowski', 5)
    response = test_app.get('/movies')
    assert response.status_code == 200
    assert b'<td>The Matrix</td>' in response.data

def test_app_function():
    # test the app.py list_all_movies function
    test_app = app.test_client()
    movie_repository = get_movie_repository()
    assert len(movie_repository.get_all_movies()) == 1
    movie_repository.create_movie('Sample movie', 'Bob Sample', 1)
    assert len(movie_repository.get_all_movies()) == 2
