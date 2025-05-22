import os


def write_to_log(log_message):
    """Writes to a log file as a side effect."""
    log_dir = "logs"
    os.makedirs(log_dir, exist_ok=True)    
    with open(os.path.join(log_dir, "collection.log"), "a") as f:
        f.write(log_message)
    
    return None


def some_func_without_side_effects():
    return None


def some_func_with_side_effects(
        logger=write_to_log("Logged from function signature")
        ):
    """Impure func with logging"""
    return None
