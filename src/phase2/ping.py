
import subprocess
from datetime import datetime

def ping_device(ip):
    """
    Ping a device and return latency (ms) and status ('UP'/'DOWN').
    """
    try:
        output = subprocess.run(["ping", "-n", "1", ip], capture_output=True)
        latency = None
        for line in output.stdout.decode().split("\n"):
            if "Average" in line or "Média" in line:  # Windows EN/PT
                latency = int(line.split(" = ")[-1].replace("ms", "").strip())
                break
        # Status is UP only if we have a valid latency
        status = "UP" if latency is not None and latency > 0 else "DOWN"
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return timestamp, latency, status
    except Exception as e:
        # If ping fails completely
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S"), None, "DOWN"