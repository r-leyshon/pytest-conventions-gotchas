"""This module will not be discovered by pytest."""
from src.fizzbuzz import fizzbuzz

def test_fizzbuzz_fizzes():
    assert fizzbuzz(3) == "fizz", "Should have fizzed."
    assert fizzbuzz(6) == "fizz", "Should have fizzed."

def test_fizzbuzz_buzzes():
    assert fizzbuzz(5) == "buzz", "Should have buzzed."
    assert fizzbuzz(10) == "buzz", "Should have buzzed."

def test_fizzbuzz_fizzbuzzes():
    assert fizzbuzz(15) == "fizzbuzz", "Should have fizzbuzzed."
    assert fizzbuzz(30) == "fizzbuzz", "Should have fizzbuzzed."

def test_fizzbuzz_numbers():
    assert fizzbuzz(1) == "1", "Should return number as string."
    assert fizzbuzz(2) == "2", "Should return number as string."
