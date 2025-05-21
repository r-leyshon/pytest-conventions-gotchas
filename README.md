# Pytest Conventions & Common Pitfalls

## Repo Structure

This repo uses small examples in branches. Please check them out and refer to
the README in the branches for specific guidance.

## Setup

1. Clone the repository.
2. Create a virtual environment with python 3.12 or later.
3. Install the requirements.

## Branch Overview: `main`

This branch displays a modern & minimal setup where code in the `src` directory
can be discovered by `pytest`. This code was written with python3.12 and
`pytest==8.3.5`, older versions may require a different setup.

The source code is a simple fizzbuzz function.

Note the presence of a minimal `pyproject.toml`. This config step is important
in fixing the `PYTHONPATH` so that `pytest` knows to discover code relative to
the root directory rather than `tests`.

## Instructions

Practise invocation methods from the command line. Notice the number of tests
**collected** and **executed** with each command.

1. `pytest`
2. `pytest -v`
3. `pytest --collect-only`
3. `pytest tests/test_fizzbuzz.py`
4. `pytest -v tests/test_fizzbuzz.py::test_fizzbuzz_buzzes`
5. `pytest -k 'buzzes'`

## Notes

### Test structure

* The structure of the `tests` folder mirrors `src`.
* `assert` statements include a second optional argument - a message to display
when the test fails. Feel free to expose important values with f-strings -
super helpful.
* Tests are given names that give clues to their purpose. Multiple assertions
can be grouped under the same test when multiple cases should be tested.

### Collection versus Execution

The discovery phase of a `pytest` workflow scans your repository for test
modules, classes and functions. A list of tests to run is collated before any
code is run. Once `pytest` is finished collecting tests, the test logic will
be executed.

> Collection is like creating a playlist. Execution is playing the songs.
