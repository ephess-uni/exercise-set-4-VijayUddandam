""" ex_4_3.py """
import os

try:
    from src.ex_4_0 import get_shutdown_events
    from src.ex_4_2 import logstamp_to_datetime
    from src.util import get_data_file_path
except ImportError:
    from ex_4_0 import get_shutdown_events
    from ex_4_2 import logstamp_to_datetime
    from util import get_data_file_path

# Use this FILENAME variable to test your function.
FILENAME = get_data_file_path("messages.log")
# >>>> DO NOT MODIFY CODE ABOVE <<<<


def time_between_shutdowns(logfile):
    """
    Your docstring here.  Replace the pass keyword below with your implementation.
    """
    shutdown_times = []  
    
    try:
        with open(logfile, 'r') as file: 
            for line in file: 
                if "Shutdown initiated" in line or "Shutdown complete" in line:  
                    timestamp = line.split()[1]  
                    shutdown_times.append(timestamp) 
    
        shutdown_times = [logstamp_to_datetime(timestamp) for timestamp in shutdown_times] 
    
        if len(shutdown_times) < 2: 
            print("Error: Insufficient shutdown events for comparison.")
            return None
        
        time_difference = max(shutdown_times) - min(shutdown_times)  
        return time_difference

    except FileNotFoundError:  
        print("Error: Log file not found.")
        return None

    except Exception as e:  
        print(f"An error occurred: {e}")
        return None



# >>>> The code below will call your function and print the results
if __name__ == "__main__":
    print(f'{time_between_shutdowns(FILENAME)=}')
