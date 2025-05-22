import pytest
import requests
from unittest.mock import Mock, call

from src.jokes import get_joke


@pytest.fixture(scope="function")
def ULTI_JOKE():
    return (
        "Doc, I can't stop singing 'The Green, Green Grass of Home.' That "
        "sounds like Tom Jones Syndrome. Is it common? Well, It's Not Unusual."
    )

def test_get_joke_monkeypatched(monkeypatch, ULTI_JOKE):
    # **NEW**: Create a mock that will track calls
    mock_get = Mock()
    
    # step 1: Mock the response object
    def _mock_response(*args, **kwargs):
        resp = requests.models.Response()
        resp.status_code = 200
        resp._content = ULTI_JOKE.encode("UTF8")
        resp.headers = {"Content-Type": "text/plain"}
        return resp
    
    #  **NEW**: Wrap our mock response to track calls
    def wrapped_mock(*args, **kwargs):
        mock_get(*args, **kwargs)
        return _mock_response(*args, **kwargs)
    
    # step 2: Patch requests.get with our wrapped mock
    monkeypatch.setattr(requests, "get", wrapped_mock)
    
    # step 3: Use the API
    joke = get_joke(endp="https://doesnt_exist", usr_agent="mocking_in_pytest")
    
    # step 4: Assert
    assert joke == ULTI_JOKE, f"Expected:\n'{ULTI_JOKE}\nFound:\n{joke}'"
    
    #  **NEW**: Assert that our mock was called with expected arguments
    mock_get.assert_called_once_with(
        "https://doesnt_exist",
        headers={'User-Agent': 'mocking_in_pytest', 'Accept': 'text/plain'},
        timeout=10
    )
    