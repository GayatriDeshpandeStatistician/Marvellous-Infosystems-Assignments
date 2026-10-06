
import os
import psutil
import logging
import sys

def setup_logging(log_dir):
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    log_file = os.path.join(log_dir, "proc_log.txt")

    # Add two blank lines at the top of every run
    with open(log_file, "a", encoding="utf-8") as f:
        f.write("\n\n")

    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

def log_all_processes():
    logging.info(" --- All Running Processes Logging Started --- ")
    for proc in psutil.process_iter(['pid', 'name', 'username']):
        try:
            logging.info(f"Process Name: {proc.info['name']}, PID: {proc.info['pid']}, Username: {proc.info['username']}")
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue
    logging.info(" --- All Running Processes Logging Completed --- ")

def main():
    if len(sys.argv) < 2:
        print("Usage: python assignment12_3.py <directory_name>")
        return

    dir_name = sys.argv[1]

    # Create the directory if it doesn't exist
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
        print(f"Directory '{dir_name}' created.")

    # Set up logging in the given directory
    setup_logging(dir_name)

    # Log all running processes (no filtering)
    log_all_processes()

if __name__ == "__main__":
    main()

# Command: E:\Gayatri\Python>python Assignment12_3.py DEMO
