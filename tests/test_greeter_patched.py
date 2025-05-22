"""Demonstrates how to avoid setting environment variables form tests"""

from src.greeter import greet


def test_greet_default():
    """Test the default greeting when no environment variable is set."""
    assert greet() == "Hello, World!"


def test_greet_with_user(monkeypatch):
    """Test the greeting when environment variable is set."""
    # Patch the environment variable
    monkeypatch.setenv('effective-user', 'Alice')
    assert greet() == "Hello, Alice!"


def test_greet_default_again():
    """Test the default greeting when no environment variable is set."""
    # Ensure the environment variable is not set
    assert greet() == "Hello, World!"
