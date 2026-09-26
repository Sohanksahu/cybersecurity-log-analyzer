🔐 Cybersecurity Log Analyzer

A simple Python-based cybersecurity project that analyzes system login logs and detects repeated failed login attempts.

This project is designed for beginners who want to learn the basics of Python, cybersecurity, log analysis, and GitHub.

📌 Project Overview

The Cybersecurity Log Analyzer reads a log file and analyzes failed login attempts.

It identifies:

Failed login attempts

IP addresses associated with failed attempts

Number of failed attempts from each IP address

Potentially suspicious IP addresses

An IP address is flagged when it reaches the configured threshold of failed login attempts.

🛠️ Technologies Used

Python 3

Regular Expressions (re)

Collections / Counter

File Handling

GitHub

📂 Project Structure
cybersecurity-log-analyzer/
│
├── analyzer.py
├── sample.log
├── requirements.txt
└── README.md

⚙️ How It Works

The program follows these steps:

Log File
   ↓
Read Log Entries
   ↓
Find Failed Login Attempts
   ↓
Extract IP Addresses
   ↓
Count Failed Attempts
   ↓
Check Security Threshold
   ↓
Generate Security Report

🚀 Getting Started
1. Install Python

Download and install Python 3 from the official Python website.

During installation on Windows, make sure to select:

Add Python to PATH

2. Download the Project

Download or clone this repository.

Alternatively, download the ZIP file from GitHub and extract it.

3. Open the Project Folder

Open Command Prompt inside the project folder.

The folder should contain:

analyzer.py
sample.log
requirements.txt
README.md

4. Run the Program

Run:

python analyzer.py


If you're using Windows and python doesn't work, try:

py analyzer.py

📄 Example Log

The project uses a sample log file containing entries such as:

2026-09-26 10:15:23 LOGIN_FAILED username=admin ip=192.168.1.10
2026-09-26 10:16:02 LOGIN_SUCCESS username=john ip=192.168.1.20
2026-09-26 10:17:11 LOGIN_FAILED username=admin ip=192.168.1.10

📊 Example Output
==================================================
       CYBERSECURITY LOG ANALYSIS REPORT
==================================================

Failed Login Attempts:
IP Address: 192.168.1.10 | Attempts: 4
IP Address: 10.0.0.15 | Attempts: 1

Potentially Suspicious IPs:
[ALERT] 192.168.1.10 - 4 failed login attempts

🚨 Detection Rule

The current program uses a threshold of:

THRESHOLD = 3


If an IP address has 3 or more failed login attempts, the program reports it as potentially suspicious.

This is a simple demonstration rule and should not be treated as a complete intrusion-detection system.

🎯 Learning Objectives

This project demonstrates:

Python programming fundamentals

Reading files in Python

Regular expressions

Extracting information from logs

Counting events

Basic security monitoring

Detecting suspicious authentication activity

Organizing a GitHub project

🔮 Future Improvements

Possible improvements include:

Add a graphical dashboard

Store results in SQLite

Analyze larger log files

Add date/time filtering

Detect multiple types of suspicious activity

Generate PDF security reports

Add email notifications for alerts

Add unit tests

Add configuration files

Add visualization and charts

⚠️ Disclaimer

This project is intended for educational and defensive cybersecurity purposes.

Use it only with logs and systems that you own or are authorized to monitor.

👨‍💻 Author

Created as a beginner cybersecurity project to practice Python, security monitoring, and GitHub.

⭐ If you found this project useful, consider giving the repository a star!
