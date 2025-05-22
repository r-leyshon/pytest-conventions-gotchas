# Pytest Conventions & Common Pitfalls

## Repo Structure

This repo uses small examples in branches. Please check them out and refer to
the README in the branches for specific guidance.

## Setup

1. Clone the repository.
2. Create a virtual environment with python 3.12 or later.
3. Install the requirements.

## Branch Overview: `6-monkeypatch`

The source code was lifted from a more detailed blog comparing
[mocking in python](https://thedatasavvycorner.com/blogs/15-pytest-mocking).

The `get_joke()` function will return a terrible but random dad joke whenever
it's run. This is:
* Hard to assert (random)
* At risk of being a flaky test (makes network calls).

To test this and keep our tests isolated, we need to patch. Luckily, `pytest`
includes the `monkeypatch` fixture.

## Instructions

1. Note this branch introduces a new dependency, so please re-install from 
`requirements.txt`.
2. Observe the 4 step plan to mocking with `pytest` in `test_jokes.py`.
3. See how call verification can be implemented with `unittest` in `test_jokes_assert_called.py`.

## Notes

### Test structure

The repository contains two main test files demonstrating different approaches
to mocking in pytest:

1. `test_jokes.py`: Shows basic mocking using `monkeypatch` fixture
   - Demonstrates how to mock HTTP responses
   - Uses a fixture to provide test data

2. `test_jokes_assert_called.py`: Shows advanced mocking with call verification
   - Uses `unittest.mock.Mock` to track function calls
   - Demonstrates how to verify that mocked functions are called with correct
   arguments

### What is a Test Double?

A test double is a replacement object used in testing that stands in for a real
object. Think of it like a stunt double in movies - it looks like the real
thing but is used in situations where using the real thing would be impractical
or risky. In our case:

- The real `requests.get()` makes actual HTTP calls to the internet
- Our test double (the mock) pretends to be `requests.get()` but returns predefined responses
- This makes our tests:
  - Faster (no network calls)
  - Reliable (no dependency on external services)
  - Predictable (we know exactly what response we'll get)

In `test_jokes.py`, we create a simple test double that just returns a fixed
response. In `test_jokes_assert_called.py`, we use a more sophisticated test
double that can also track how it's used.

### Mocking vs Patching

While these terms are often used interchangeably, there are subtle differences:

- **Patching** refers to the act of replacing a real object with a test double.
In pytest, this is typically done using the `monkeypatch` fixture to
temporarily replace objects during test execution.

- **Mocking** is a specific type of patching where we create a test double that
can track how it's used (like counting calls, recording arguments, etc.). This
is what we do with `unittest.mock.Mock` in `test_jokes_assert_called.py`.
