""" ex_4_1.py """
import os

try:
    from src.ex_4_0 import get_shutdown_events
    from src.util import get_data_file_path
except ImportError:
    from ex_4_0 import get_shutdown_events
    from util import get_data_file_path

# Use this FILENAME variable to test your function.
FILENAME = get_data_file_path('messages.log')
# >>>> DO NOT MODIFY CODE ABOVE <<<<


def num_shutdowns(logfile):
    """
    Your docstring here.  Replace the pass keyword below with your implementation.
    """
    with open(logfile, 'r') as file:
        log_data = file.readlines()

    shutdown_count = 0
    found_initiated = False

    for line in log_data:
        if "Shutdown initiated" in line:
            found_initiated = True
        elif "Shutdown complete" in line and found_initiated:
            shutdown_count += 1
            found_initiated = False

    return shutdown_count


# >>>> The code below will call your function and print the results
if __name__ == "__main__":
    print(f'{num_shutdowns(FILENAME)=}')