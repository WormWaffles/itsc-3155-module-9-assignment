from flask.testing import FlaskClient
# TODO: Feature 3

@pytest.fixture()
def test_search():
    response = test_app.get('/movies/search')
