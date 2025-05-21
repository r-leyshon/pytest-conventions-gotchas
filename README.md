# Pytest Conventions & Common Pitfalls

## Repo Structure

This repo uses small examples in branches. Please check them out and refer to
the README in the branches for specific guidance.

## Setup

1. Clone the repository.
2. Create a virtual environment with python 3.12 or later.
3. Install the requirements.

## Branch Overview: `3-test-classes`

The source code is a simple fizzbuzz function. The tests demonstrate how to use
test classes to organize related test cases and provide fine-grained control over
test execution.

### Test Class Organization

The tests are organized in a `TestFizzbuzz` class, which provides several
benefits:

1. **Logical Grouping**: All tests related to the fizzbuzz function are grouped
together
2. **Fine-grained Execution**: You can run specific test methods using the
class path:
```bash
pytest -v tests/test_fizzbuzz.py::TestFizzbuzz::test_fizzbuzz_fizzbuzzes
```
