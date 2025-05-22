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
