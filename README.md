# Pytest Conventions & Common Pitfalls

## Repo Structure

This repo uses small examples in branches. Please check them out and refer to
the README in the branches for specific guidance.

## Setup

1. Clone the repository.
2. Create a virtual environment with python 3.12 or later.
3. Install the requirements.

## Branch Overview: `7-dependencies-between-tests`

Install the updated dependencies.

This branch demonstrates the importance of test isolation and proper
environment variable handling in pytest.

### Test Modules

The branch contains three test modules:

1. `test_greeter.py` and `test_greeter_reversed.py` - Demonstrates poor
practice by directly setting environment variables in tests. This causes
interdependencies between the tests.
2. `test_greeter_patched.py` - Shows the correct approach using pytest's
monkeypatch fixture

### Best Practices

- Never modify environment variables directly in tests as it creates
dependencies between tests.
- Use pytest's `monkeypatch` fixture to temporarily modify environment
variables.
- This ensures test isolation and prevents test order dependencies

### Running Tests with Random Order

To help detect interdependencies in your test suite, install the
`pytest-randomly` plugin, which will run the test suite in a different order
each time. 
