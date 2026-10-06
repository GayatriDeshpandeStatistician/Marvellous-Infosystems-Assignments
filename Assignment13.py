Assignment13

import os
import hashlib
import time
import smtplib
import logging
from email.message import EmailMessage
from sys import argv
from datetime import datetime

def hashfile(path, blocksize=1024):
    with open(path, 'rb') as afile:
        hasher = hashlib.md5()
        buf = afile.read(blocksize)
        while buf:
            hasher.update(buf)
            buf = afile.read(blocksize)
    return hasher.hexdigest()

def findDup(path):
    if not os.path.isabs(path):
        path = os.path.abspath(path)

    if not os.path.isdir(path):
        logging.error("Invalid path provided.")
        return {}

    dups = {}
    for dirName, subdirs, fileList in os.walk(path):
        for filen in fileList:
            full_path = os.path.join(dirName, filen)
            try:
                file_hash = hashfile(full_path)
                if file_hash in dups:
                    dups[file_hash].append(full_path)
                else:
                    dups[file_hash] = [full_path]
            except Exception as e:
                logging.error(f"Error reading file {full_path}: {e}")
    return dups

def deleteDuplicates(dups):
    results = list(filter(lambda x: len(x) > 1, dups.values()))
    deleted_files = []

    for result in results:
        for file_path in result[1:]:
            try:
                os.remove(file_path)
                deleted_files.append(file_path)
                logging.info(f"Deleted Duplicate: {file_path}")
            except Exception as e:
                logging.error(f"Error deleting {file_path}: {e}")
    return deleted_files

def send_email(receiver_email, log_file_path):
    sender_email = "abc@gmail.com"
    sender_password = "yourapppassword"

    msg = EmailMessage()
    msg['Subject'] = 'Duplicate File Removal Log'
    msg['From'] = sender_email
    msg['To'] = receiver_email

    msg.set_content("Please find the attached log file containing the details of duplicate file removal.")

    with open(log_file_path, 'rb') as f:
        msg.add_attachment(f.read(), maintype='text', subtype='plain', filename=os.path.basename(log_file_path))

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(sender_email, sender_password)
            smtp.send_message(msg)
    except Exception as e:
        logging.error(f"Error sending email: {e}")

def create_log_file():
    if not os.path.exists("Marvellous"):
        os.mkdir("Marvellous")
    log_file = datetime.now().strftime("Marvellous/log_%Y-%m-%d_%H-%M-%S.txt")
    return log_file

def main():
    if len(argv) != 4:
        print("Usage: python Assignment14_DuplicateCleaner.py <directory_path> <interval_minutes> <receiver_email>")
        exit()

    directory = argv[1]
    interval = int(argv[2])
    receiver_email = argv[3]

    while True:
        log_file = create_log_file()
        logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s - %(message)s')

        logging.info("==== Duplicate File Removal Process Started ====")
        dups = findDup(directory)
        if not dups:
            logging.info("No duplicate files found.")
        else:
            logging.info("Duplicate files found. Proceeding with deletion...")
            deleteDuplicates(dups)

        logging.info("==== Process Completed ====\n")

        send_email(receiver_email, log_file)

        time.sleep(interval * 60)

if __name__ == "__main__":
    main()

#python Assignment13.py "E:/Data/Demo" 50 xyz@gmail.com
