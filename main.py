import os
import sqlite3
from db_extractor import extract_deleted_messages
from report_generator import generate_report
from gui import start_gui

def main():
    print("WhatsApp Forensic Tool")
    backup_file = input("Enter the path to the WhatsApp backup file: ")

    if not os.path.exists(backup_file):
        print("Backup file not found!")
        return

    conn = sqlite3.connect(backup_file)
    cursor = conn.cursor()

    messages = extract_deleted_messages(cursor)
    generate_report(messages)

    print("Analysis complete. Report generated.")

if __name__ == "__main__":
    start_gui()
