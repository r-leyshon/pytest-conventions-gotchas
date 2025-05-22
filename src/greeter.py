import os

def set_user(username: str) -> None:
    """Sets the effective-user environment variable."""
    os.environ['effective-user'] = username

def greet() -> str:
    """Returns a greeting message. 

    If effective-user is set, uses that username, otherwise returns a
    generic hello world message.
    """
    effective_user = os.environ.get('effective-user')
    if effective_user:
        return f"Hello, {effective_user}!"
    return "Hello, World!" 
