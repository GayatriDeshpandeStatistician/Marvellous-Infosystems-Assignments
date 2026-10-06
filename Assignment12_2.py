# 12_2 : Design An Automation Script which accpets the process name and displays the information of that process if it is runnning

import psutil
import logging
import os
import sys

# Setup logging to logs/proc_log.txt
def setup_logging():
    if not os.path.exists("logs"):
        os.makedirs("logs")
    log_file = os.path.join("logs", "proc_log.txt")

    with open(log_file, "a", encoding="utf-8") as f:
        f.write("\n\n")

    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

# Get and log processes by filter
def log_filtered_processes(process_name):
    found = False
    for proc in psutil.process_iter(['pid', 'name', 'username']):
        try:
            pinfo = proc.info
            if pinfo['name'] and process_name.lower() in pinfo['name'].lower():
                logging.info(f"Process Name: {pinfo['name']}, PID: {pinfo['pid']}, Username: {pinfo['username']}")
                found = True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue

    if not found:
        logging.info(f"No running process found with name containing: {process_name}")

# Main driver function
def main():
    setup_logging()
    logging.info(" --- Filtered Process Logging Started --- ")

    # Check for process name in command-line
    if len(sys.argv) < 2:
        logging.error("No process name provided in command-line arguments.")
        return

    process_name = sys.argv[1]
    log_filtered_processes(process_name)

    logging.info("--- Filtered Process Logging Completed ---")

if __name__ == "__main__":
    main()

# Command : E:\Gayatri\Python>python Assignment12_2.py Notepad
