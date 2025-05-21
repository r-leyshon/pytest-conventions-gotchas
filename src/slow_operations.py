import time

def slow_operation():
    """
    A function that simulates a slow operation by sleeping for 5 seconds.
    
    Returns:
        str: A message indicating the operation is complete
    """
    time.sleep(5)  # Sleep for 5 seconds
    return "Slow operation completed!" 
