import os
import subprocess

def search_files(query):
    print(f"Searching for files containing '{query}'...")
    for root, dirs, files in os.walk("."):
        for file in files:
            if query.lower() in file.lower():
                print(os.path.join(root, file))

def open_file(filepath):
    try:
        if os.path.exists(filepath):
            print(f"Opening file: {filepath}")
            if os.name == 'nt':  # Windows
                os.startfile(filepath)
            elif os.name == 'posix':  # Mac or Linux
                subprocess.call(['open', filepath])
        else:
            print("File not found.")
    except Exception as e:
        print(f"Error: {e}")
