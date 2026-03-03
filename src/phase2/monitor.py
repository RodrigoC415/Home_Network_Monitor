import time
from ping import ping_device
from database import Database

# Devices to monitor
devices = {
    "Primary Router": "192.168.1.1",
    "Secondary Router": "192.168.3.1",
    "Internet Test": "8.8.8.8"
}

# Connection to database
db = Database(password="postgres")

# Interval in seconds
interval = 30

# Main monitoring loop
try:
    while True:
        for name, ip in devices.items():
            timestamp, latency, status = ping_device(ip)
            
            db.insert_metric(name, latency, status)               #Insert in database
            print(f"{timestamp} | {name} | {status} | {latency} ms")
        
        time.sleep(interval)

except KeyboardInterrupt:
    print("Monitoring stopped")

finally:
    db.close()