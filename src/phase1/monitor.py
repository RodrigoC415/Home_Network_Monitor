import time
from collector.ping import ping_device
from database.storage import write_csv

# Devices to monitor
devices = {
    "Primary Router": "192.168.1.1",
    "Secondary Router": "192.168.3.1",
    "Internet Test": "8.8.8.8"
}

# CSV file path
csv_file = "data/metrics.csv"

# Interval in seconds
interval = 30

# Main monitoring loop
while True:
    for name, ip in devices.items():
        timestamp, latency, status = ping_device(ip)
        write_csv(csv_file, [timestamp, name, latency, status])
        print(f"{timestamp} | {name} | {status} | {latency} ms")
    time.sleep(interval)