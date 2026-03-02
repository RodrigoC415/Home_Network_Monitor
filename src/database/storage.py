import csv
import os

def write_csv(file_path, data):
    """
    Write a row of data to CSV file. Creates file if it does not exist.
    Data should be a list: [timestamp, device_name, latency, status]
    """
    file_exists = os.path.isfile(file_path)
    with open(file_path, "a", newline="") as f:       #Open file in append mode
        writer = csv.writer(f)
        if not file_exists:
            # Write header if file is new
            writer.writerow(["timestamp", "device_name", "latency_ms", "status"])
        writer.writerow(data)