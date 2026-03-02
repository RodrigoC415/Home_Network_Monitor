# Home Network Monitoring System

## Overview
The goal of this project is to monitor different routers in the local network, recording metrics such as latency and availability.
The objective is to creat historic data to analyse the performance of the network and detect possible breakdowns.

## Technologies
- Python (monitoring and analysis)
- ICMP/Ping
- PostgreSQL (database)
- Grafana (Dashboard)

## Devices Monitored
- Primary Router
- Secondary Router
- 8.8.8.8 (internet connectivity test)


## Phase 1 – Basic Network Monitoring

**Objective:**  
Create a Python script to monitor devices in the local network, collect latency and availability data, and save it in a CSV file.

## Architecture 

- monitor.py calls ping.py functions  
- Results are stored using storage.py into CSV  

**Implementation:**  
- **`ping.py`** – Function `ping_device(ip)` pings a device and returns:
  - Timestamp
  - Latency (ms)
  - Status (`UP` / `DOWN`)
- **`storage.py`** – Function `write_csv(file_path, data)` writes results to CSV, creating the file with header if it does not exist
- **`monitor.py`** – Loops through devices, calls `ping_device()`, writes results to CSV, and prints output to terminal

**CSV file example:**

![Phase 1 CSV](docs/phase1_csv.png)

**Terminal output example:**

![Phase 1 Terminal Output](docs/phase1_terminal.png)

**Notes / Challenges:**  
- Latency extraction works for both English and Portuguese Windows ping output  
- Status is marked as `DOWN` only if latency could not be measured  
- In some rare cases, a latency value of 0ms may be returned. Although this is technically possible in very fast local networks, it can also indicate a parsing or measurement issue. If incorrectly interpreted as `DOWN`, this could lead to false alerts. Additional validation logic may be required in future versions.

## How To Run (Version 1)
1. Go to the `src` folder
2. Check that the IPs of the devices in monitor.py are correct for your network.
3. Run the monitoring script: python monitor.py
4. he CSV file will be created at data/metrics.csv and results will be printed in the terminal
5. Stop monitoring anytime with Ctrl+C.

## Future Improvements
...