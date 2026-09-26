import re
from collections import Counter


LOG_FILE = "sample.log"
THRESHOLD = 3


def read_log_file(filename):
    try:
        with open(filename, "r") as file:
            return file.readlines()
    except FileNotFoundError:
        print(f"Error: {filename} was not found.")
        return []


def find_failed_logins(log_lines):
    failed_ips = []

    for line in log_lines:
        if "LOGIN_FAILED" in line:
            match = re.search(r"ip=(\d+\.\d+\.\d+\.\d+)", line)

            if match:
                ip = match.group(1)
                failed_ips.append(ip)

    return failed_ips


def analyze_ips(failed_ips):
    return Counter(failed_ips)


def generate_report(ip_counts):
    print("\n" + "=" * 50)
    print("       CYBERSECURITY LOG ANALYSIS REPORT")
    print("=" * 50)

    if not ip_counts:
        print("No failed login attempts detected.")
        return

    print("\nFailed Login Attempts:")

    for ip, count in ip_counts.items():
        print(f"IP Address: {ip} | Attempts: {count}")

    print("\nPotentially Suspicious IPs:")

    suspicious_found = False

    for ip, count in ip_counts.items():
        if count >= THRESHOLD:
            print(f"[ALERT] {ip} - {count} failed login attempts")
            suspicious_found = True

    if not suspicious_found:
        print("No suspicious IPs detected.")


def main():
    logs = read_log_file(LOG_FILE)

    if not logs:
        return

    failed_logins = find_failed_logins(logs)
    ip_counts = analyze_ips(failed_logins)

    generate_report(ip_counts)


if __name__ == "__main__":
    main()
