import os
from src.greeter import set_user, greet

def test_greeter_no_env_var():
    # Test default greeting
    assert greet() == "Hello, World!", "Expected msg not encountered."


def test_greeter_with_env_var():
    # Test greeting with user set
    set_user("Alice")
    assert greet() == "Hello, Alice!", "Expected msg not encountered."
    