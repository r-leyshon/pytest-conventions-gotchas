import pytest
from src.fizzbuzz import fizzbuzz


@pytest.fixture
def fizzy_numbers():
    return [3, 6]


@pytest.fixture
def buzzy_numbers():
    return [5, 10]


@pytest.fixture
def fizzbuzzy_numbers():
    return [15, 30]


@pytest.fixture
def quiet_numbers():
    return [1, 2, 4, 7, 8]


def test_fizzbuzz_fizzes(fizzy_numbers):
    for number in fizzy_numbers:
        assert fizzbuzz(number) == "fizz", f"Should have fizzed for {number}"


def test_fizzbuzz_buzzes(buzzy_numbers):
    for number in buzzy_numbers:
        assert fizzbuzz(number) == "buzz", f"Should have buzzed for {number}"


def test_fizzbuzz_fizzbuzzes(fizzbuzzy_numbers):
    for number in fizzbuzzy_numbers:
        assert fizzbuzz(number) == "fizzbuzz", f"Should have fizzbuzzed for {number}"


def test_fizzbuzz_numbers(quiet_numbers):
    for number in quiet_numbers:
        assert fizzbuzz(number) == str(number), f"Should return {number} as string"
