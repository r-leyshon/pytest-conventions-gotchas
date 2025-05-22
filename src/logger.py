import os


def write_to_log(log_message, pth):
    """Writes to a log file as a side effect.
    
    Args:
        log_message (str): The message to write to the log file
        pth (str): The path where the log file should be created

    Raises:
        ValueError: If the provided path does not end with '.log'
    """
    if not pth.endswith('.log'):
        raise ValueError("Log file path must end with '.log'")
        
    os.makedirs(os.path.dirname(pth), exist_ok=True)    
    with open(pth, "a") as f:
        f.write(log_message)
    
    return None 
