from src.fizzbuzz import fizzbuzz

class TestFizzbuzz:
    """Grouping all tests for function fizzbuzz."""
    def test_fizzbuzz_fizzes(self):
        assert fizzbuzz(3) == "fizz", "Should have fizzed."
        assert fizzbuzz(6) == "fizz", "Should have fizzed."

    def test_fizzbuzz_buzzes(self):
        assert fizzbuzz(5) == "buzz", "Should have buzzed."
        assert fizzbuzz(10) == "buzz", "Should have buzzed."

    def test_fizzbuzz_fizzbuzzes(self):
        assert fizzbuzz(15) == "fizzbuzz", "Should have fizzbuzzed."
        assert fizzbuzz(30) == "fizzbuzz", "Should have fizzbuzzed."

    def test_fizzbuzz_numbers(self):
        assert fizzbuzz(1) == "1", "Should return number as string."
        assert fizzbuzz(2) == "2", "Should return number as string."
