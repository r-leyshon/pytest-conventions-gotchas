# Pytest Conventions & Common Pitfalls

## Repo Structure

This repo uses small examples in branches. Please check them out and refer to
the README in the branches for specific guidance.

## Setup

1. Clone the repository.
2. Create a virtual environment with python 3.12 or later.
3. Install the requirements.

## Branch Overview: `5-fixtures`

This branch demonstrates:

The src code remains unchanged from `main` branch. 

The tests have been updated to demonstrate the use of fixtures.

## Instructions

1. Review the example fixtures in `conftest.py`
2. Study the test files to see how fixtures are used

## Notes

* **Autouse Fixtures** - including `autouse=True` will instruct `pytest` to
inject the fixture into every test module. This reduces boilerplate but also
makes the test less explicit. If this is not needed it can also reduce the
performance of the test suite.

* **Fixture Scopes** - fixtures can be scoped at different levels:
  - `function` (default): fixture is created for each test function
  - `class`: fixture is created once per test class
  - `module`: fixture is created once per module
  - `session`: fixture is created once for the entire test session
  - `package`: fixture is created once per package

Choosing the right scope is crucial for test performance and resource
management. Use broader scopes (module/session) for expensive setup operations,
but be careful about test isolation. Narrower scopes (function) provide better
isolation but may impact performance if the setup is expensive.
