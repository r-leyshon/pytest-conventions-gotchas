"""Module won't collect because no compliant test names."""
from src.fizzbuzz import fizzbuzz

def fizzbuzz_fizzes():
    assert fizzbuzz(3) == "fizz", "Should have fizzed."
    assert fizzbuzz(6) == "fizz", "Should have fizzed."

def fizzbuzz_buzzes():
    assert fizzbuzz(5) == "buzz", "Should have buzzed."
    assert fizzbuzz(10) == "buzz", "Should have buzzed."

def fizzbuzz_fizzbuzzes():
    assert fizzbuzz(15) == "fizzbuzz", "Should have fizzbuzzed."
    assert fizzbuzz(30) == "fizzbuzz", "Should have fizzbuzzed."

def test_fizzbuzz_numbers():
    assert fizzbuzz(1) == "1", "Should return number as string."
    assert fizzbuzz(2) == "2", "Should return number as string."
