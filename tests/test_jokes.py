import pytest
import requests

from src.jokes import get_joke


@pytest.fixture(scope="function")
def ULTI_JOKE():
    return (
        "Doc, I can't stop singing 'The Green, Green Grass of Home.' That "
    "sounds like Tom Jones Syndrome. Is it common? Well, It's Not Unusual."
    )

def test_get_joke_monkeypatched(monkeypatch, ULTI_JOKE):
    # step 1: Mock the response object
    def _mock_response(*args, **kwargs):
        resp = requests.models.Response()
        resp.status_code = 200
        resp._content = ULTI_JOKE.encode("UTF8")
        resp.headers = {"Content-Type": "text/plain"}
        return resp
    
    # step 2: Patch requests.get
    monkeypatch.setattr(requests, "get", _mock_response)
    # step 3: Use the API
    joke = get_joke()
    # step 4: Assert
    assert joke == ULTI_JOKE, f"Expected:\n'{ULTI_JOKE}\nFound:\n{joke}'"
    # will also work for json format
    joke = get_joke(f="application/json")
    assert joke == ULTI_JOKE, f"Expected:\n'{ULTI_JOKE}\nFound:\n{joke}'"
