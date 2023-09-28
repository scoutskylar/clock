from app import *
import re

def test_timestamp():
    assert type(generate_timestamp()) == str

def test_index():
    app.config["TESTING"] = True
    client = app.test_client()
    response = client.get("/")
    test_regex = re.compile("The UNIX timestamp on the server when generating this page was \\d+\\.")
    print(test_regex)
    assert test_regex.search(str(response.data))
