# Task 4 – Smart Keylogger (Without External Libraries)

##  Project Overview

This project is a **simple keylogging and word-tracking application** created using Python. Unlike traditional keyloggers that require external libraries such as `pynput`, this program works **without installing any third-party modules**. It logs the words entered by the user in the terminal and stores them in a log file.

This tool is intended for **educational purposes**, to understand how input handling, file logging, and log rotation work in Python. It does **not** run silently in the background and does **not capture system-wide keystrokes**, making it safe and legal to use.

---

##  Features

✔ Logs each typed word with timestamps  
✔ Stores all logs in a text file  
✔ Automatically creates a backup when the log file becomes too large (Log Rotation)  
✔ No external libraries required (`pynput` not needed)  
✔ Works on Linux, Windows, and macOS  
✔ Simple and beginner-friendly code

---

## How It Works

1. The program asks the user to type words in the terminal.
2. Each word typed is saved into a log file named **`smart_keylog.txt`**.
3. A timestamp is added to every logged entry.
4. When the log file size reaches **5 KB**, it is renamed as:
