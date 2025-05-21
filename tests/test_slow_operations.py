"""Tests for slow operations module. Note the useful mark."""
import pytest
from src.slow_operations import slow_operation

@pytest.mark.slow
def test_slow_operation():
    """Test that slow operation completes and returns expected result."""
    result = slow_operation()
    assert result == "Slow operation completed!" 
