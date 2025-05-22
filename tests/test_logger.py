import os

import pytest

from src.logger import write_to_log


def test_write_to_log_with_tmp(tmp_path):
    test_message = "Test log message\n"
    log_path = os.path.join(tmp_path, "test.log")    
    write_to_log(test_message, log_path)
    
    # Verify the log file was created
    assert os.path.exists(log_path), f"Expected file at {log_path} to exist."
    
    # Read and verify the content
    with open(log_path, "r") as f:
        content = f.read()
        assert content == test_message, f"Expected log equal to {test_message}"


def test_write_to_log_invalid_extension(tmp_path):
    # Test message
    test_message = "Test log message\n"
    invalid_path = os.path.join(tmp_path, "test.xlsx")
    
    # Verify that writing to a non-.log file raises ValueError
    with pytest.raises(ValueError, match="Log file path must end with '.log'"):
        write_to_log(test_message, invalid_path)
        