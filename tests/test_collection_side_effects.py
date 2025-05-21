from src.collection_side_effects import (
    some_func_with_side_effects,
    some_func_without_side_effects,
)


def test_with_side_effects():
    """
    This test uses a function with a default argument that has side effects.
    The log file will be written to during collection because the default argument
    is evaluated when the function is defined.
    """
    result = some_func_with_side_effects()
    assert result is None


def test_without_side_effects():
    """
    This test uses a function without any side effects in its signature.
    No log file will be written during collection.
    """
    result = some_func_without_side_effects()
    assert result is None 
