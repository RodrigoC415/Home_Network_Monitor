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


# Phase 1 – Basic Network Monitoring

## Objective
Create a Python script to monitor devices in the local network, collect latency and availability data, and store it in a CSV file.

## Architecture

![Phase 1 Architecture](docs/phase1_architecture.png)

### Flow Description
- `monitor.py` controls the monitoring loop  
- `ping.py` handles the ICMP requests and latency parsing  
- `storage.py` writes the collected data into a CSV file  
- Data is stored in `metrics.csv` for historical tracking  

## Implementation
- **`ping.py`** – Function `ping_device(ip)` pings a device and returns:
  - Timestamp
  - Latency (ms)
  - Status (`UP` / `DOWN`)
- **`storage.py`** – Function `write_csv(file_path, data)` writes results to CSV, creating the file with header if it does not exist
- **`monitor.py`** – Loops through devices, calls `ping_device()`, writes results to CSV, and prints output to terminal

## Results

### CSV File Example
![Phase 1 CSV](docs/phase1_csv.png)

### Terminal Output Example
![Phase 1 Terminal Output](docs/phase1_terminal.png)

## Challenges & Notes
- Latency extraction works for both English and Portuguese Windows ping output  
- Status is marked as `DOWN` only if latency could not be measured  
- A latency value of 0ms may occur in extremely fast local networks but may also indicate parsing issues. If incorrectly interpreted as `DOWN`, this could generate false alerts. Future versions may include stricter validation logic.

## How To Run (Version 1)

1. Go to the `src` folder  
2. Check that the IP addresses in `monitor.py` match your local network  
3. Run the monitoring script: python monitor.py
4. The CSV file will be created at data/metrics.csv and results will be printed in the terminal
5. Stop monitoring anytime with Ctrl+C.