# Pytest Conventions & Common Pitfalls

## Repo Structure

This repo uses small examples in branches. Please check them out and refer to
the README in the branches for specific guidance.

## Setup

1. Clone the repository.
2. Create a virtual environment with python 3.12 or later.
3. Install the requirements.

## Branch Overview: `7-tmp`

This branch demonstrates how to properly handle file system side effects in
pytest tests, specifically focusing on log file cleanup. It builds upon the
issues shown in branch `2-collection-side-effects` by implementing proper test
cleanup.

- Uses pytest's built-in `tmp_path` fixture to create temporary directories for
test files
- Automatically cleans up test artifacts after each test execution
- Demonstrates proper file handling in tests that need to write to the
filesystem
- Shows how to verify file contents while maintaining test isolation

## Instructions

1. Run the tests to see how temporary files are handled:
   ```bash
   pytest tests/test_logger.py -v
   ```
2. Notice that no log files remain after test execution
3. Compare this implementation with branch `2-collection-side-effects`.

