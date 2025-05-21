# Pytest Conventions & Common Pitfalls

## Repo Structure

This repo uses small examples in branches. Please check them out and refer to
the README in the branches for specific guidance.

## Setup

1. Clone the repository.
2. Create a virtual environment with python 3.12 or later.
3. Install the requirements.

## Branch Overview: `4-deselecting-tests`

This branch demonstrates how to selectively run or skip tests.

The src code includes `fizzbuzz` from `main` branch. But there is also a module
of 'slow' code that we may wish to skip.

## Instructions

1. Run all tests:
   ```bash
   pytest -v
   ```

2. Run all tests except slow ones:
   ```bash
   pytest -m "not slow"
   ```

3. Run only slow tests:
   ```bash
   pytest -m "slow"
   ```

4. View available markers and their descriptions:
   ```bash
   pytest --markers
   ```

## Using Marks in Your Test Suite

Marks are a powerful way to categorize and control test execution. Here are
some common use cases:

1. **Slow Tests** (implemented in this branch)
   - Mark tests that take a long time to run
   - Skip during development with `-m "not slow"`

2. **Integration Tests**
   - Mark tests that require external services or complex setup
   - Example: `@pytest.mark.integration`

3. **Smoke Tests**
   - Mark critical path tests that should run first
   - Example: `@pytest.mark.smoke`

4. **Feature-specific Tests**
   - Group tests by feature or component
   - Example: `@pytest.mark.api`, `@pytest.mark.ui`

5. **Environment-specific Tests**
   - Mark tests that should only run in certain environments
   - Example: `@pytest.mark.production`, `@pytest.mark.staging`

### Registering Custom Marks

Before using any custom mark, you must register it in your `pyproject.toml`:

```toml
[tool.pytest.ini_options]
markers = [
    "slow: marks tests as slow (deselect with '-m \"not slow\"')",
    "integration: marks tests as integration tests",
    "smoke: marks critical path tests",
    "api: marks API-related tests",
    "ui: marks UI-related tests"
]
```

## Notes

- Marks must be registered before use to avoid warnings
- You can combine marks using `and`, `or`, and `not`
- Example: `pytest -m "smoke and not slow"` runs only smoke tests that aren't
slow
