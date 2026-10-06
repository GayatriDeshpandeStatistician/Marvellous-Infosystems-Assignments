# Design an automation script which displays the information of running processess as Name Pid Username
import psutil
import logging
import os
import sys

# Setup log file
def setup_logging():
    if not os.path.exists("logs"):
        os.makedirs("logs")
    log_file = os.path.join("logs", "proc_log.txt")
    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

# Fetch processes (all or filtered)
def ProcessDisplay(filter_name=None):
    listprocess = []
    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['pid', 'name', 'username'])
            if filter_name:
                if pinfo['name'] and filter_name.lower() in pinfo['name'].lower():
                    listprocess.append(pinfo)
            else:
                listprocess.append(pinfo)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue
    return listprocess

# Main function
def main():
    setup_logging()
    logging.info(" --- Process Monitor Started --- ")

    # Command-line argument handling
    filter_name = None
    if len(sys.argv) > 1:
        filter_name = sys.argv[1]  # first argument is the filter name (e.g., Notepad)

    listprocess = ProcessDisplay(filter_name)

    for elem in listprocess:
        logging.info(f"Process Name: {elem['name']}, PID: {elem['pid']}, Username: {elem['username']}")

    logging.info("--- Process Monitor Completed ---")

if __name__ == "__main__":
    main()

## Command - C:\Users\admin>E:
## Command - E:\Gayatri\Python>python assignment12_1.py