import pytest
from app import *
import re

@pytest.fixture()
def client():
    app.config['TESTING'] = True
    return app.test_client()

def test_timestamp():
    assert type(generate_timestamp()) == str

def test_index(client):
    response = client.get('/')
    test_regex = re.compile('The UNIX timestamp on the server when generating this page was \\d+\\.')
    print(test_regex)
    assert test_regex.search(str(response.data))

def test_custom_clock_get(client):
    response = client.get('/custom')
    assert 'Error' in str(response.data)

def test_custom_clock_post(client):
    response = client.post('/custom', data={'user': 'Bob Sample'})
    assert 'Welcome, Bob Sample!' in str(response.data)
