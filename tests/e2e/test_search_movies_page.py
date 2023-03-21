from flask.testing import FlaskClient
from app import app
# TODO: Feature 3

@pytest.fixture()
def test_search():
    test_app = app.test_client()
    response = test_app.get('/movies/search')
