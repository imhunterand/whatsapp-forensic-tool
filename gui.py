import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import os
import sqlite3
from db_extractor import extract_deleted_messages
from report_generator import generate_report

def start_gui():
    def load_backup():
        file_path = filedialog.askopenfilename()
        if file_path:
            backup_entry.delete(0, tk.END)
            backup_entry.insert(0, file_path)

    def analyze_backup():
        backup_file = backup_entry.get()
        if not os.path.exists(backup_file):
            messagebox.showerror("Error", "Backup file not found!")
            return

        conn = sqlite3.connect(backup_file)
        cursor = conn.cursor()

        messages = extract_deleted_messages(cursor)
        generate_report(messages)

        messagebox.showinfo("Success", "Analysis complete. Report generated.")

    root = tk.Tk()
    root.title("WhatsApp Forensic Tool")

    tk.Label(root, text="WhatsApp Backup File:").pack(padx=10, pady=5)
    backup_entry = tk.Entry(root, width=50)
    backup_entry.pack(padx=10, pady=5)

    tk.Button(root, text="Browse", command=load_backup).pack(padx=10, pady=5)
    tk.Button(root, text="Analyze", command=analyze_backup).pack(padx=10, pady=10)

    root.mainloop()

if __name__ == "__main__":
    start_gui()
