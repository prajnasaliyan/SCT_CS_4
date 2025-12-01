from datetime import datetime
import os

LOG_FILE = "smart_keylog.txt"
MAX_SIZE = 5 * 1024  # 5KB log file size limit
buffer = ""  # stores typed characters before saving as a word

def check_log_size():
    """Rotate log file if it exceeds size limit."""
    if os.path.exists(LOG_FILE) and os.path.getsize(LOG_FILE) > MAX_SIZE:
        backup_name = LOG_FILE.replace(".txt", "_backup.txt")
        os.rename(LOG_FILE, backup_name)
        print(f"Log rotated! Old log saved as: {backup_name}")

def write_log(text):
    """Write timestamped entry to file."""
    check_log_size()
    with open(LOG_FILE, "a") as f:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"{timestamp} -> {text}\n")

print("==== Smart Keylogger Started (No External Libraries) ====")
print("Type words. Press ENTER to save a word. Type 'exit' to stop.")

while True:
    user_input = input("> ")

    if user_input.lower() == "exit":
        if buffer:
            write_log(f"Word typed before exit: {buffer}")
        write_log("Keylogger stopped by user.")
        print("Stopped!")
        break

    # Log each word separately
    words = user_input.split()
    for w in words:
        write_log(f"Word typed: {w}")
