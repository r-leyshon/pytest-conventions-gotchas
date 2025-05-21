# Pytest Conventions & Common Pitfalls

## Repo Structure

This repo uses small examples in branches. Please check them out and refer to
the README in the branches for specific guidance.

## Setup

1. Clone the repository.
2. Create a virtual environment with python 3.12 or later.
3. Install the requirements.

## Branch Overview: `main`

This branch demonstrates common pitfalls in pytest, particularly focusing on
collection-time side effects.

## Instructions

1. Run the collection side effects example:
   ```bash
   pytest tests/test_collection_side_effects.py --collect-only
   ```
   Notice that the log file is created in the `logs` directory during
   collection, before any tests actually run.

2. Run a different test file:
   ```bash
   pytest tests/test_fizzbuzz.py -v
   ```
   Notice that no log file is created because the collection side effects
   module is not imported.

## Notes

### Collection-time Side Effects

The `collection_side_effects.py` module demonstrates how default arguments in
function signatures can cause side effects during pytest's collection phase.
This is particularly important to be aware of when:

- Using default arguments that have side effects
- Defining fixtures or test functions with default arguments
- Working with any code that might have side effects in function signatures

### Best Practices

To avoid collection-time side effects, consider these approaches:

If possible, consider logging only at the top level (eg in `main`), although
the required level of logging may make this challenging.

Otherwise, move function invocations to the function body:
   ```python
   # Instead of this:
   def some_func(logger=write_to_log("Logged from signature")):
       pass

   # Do this:
   def some_func(logger=None):
       if logger is None:
           logger = write_to_log("Logged from body")
       pass
   ```

This patterns ensure that side effects only occur when the function is actually
called, not during collection.
