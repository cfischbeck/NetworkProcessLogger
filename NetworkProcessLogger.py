import psutil
import datetime
import socket
import time

def get_process_info():
    connections = psutil.net_connections(kind='inet')
    log_entries = []

    for conn in connections:
        process_id = conn.pid
        if process_id is not None:
            try:
                process = psutil.Process(process_id)
                process_name = process.name()
                local_address = f"{conn.laddr.ip}:{conn.laddr.port}" if conn.laddr else "N/A"
                remote_address = f"{conn.raddr.ip}:{conn.raddr.port}" if conn.raddr else "N/A"
                protocol = "TCP" if conn.type == socket.SOCK_STREAM else "UDP"
                timestamp = datetime.datetime.now()

                log_entries.append({
                    "timestamp": timestamp,
                    "process_name": process_name,
                    "process_id": process_id,
                    "local_address": local_address,
                    "remote_address": remote_address,
                    "protocol": protocol,
                    "status": conn.status
                })
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass  # Process has been terminated or cannot be accessed

    return log_entries

def log_to_file(entries, filename="network_log.txt"):
    with open(filename, "a") as file:
        for entry in entries:
            file.write(f"{entry['timestamp']} - {entry['process_name']} ({entry['process_id']}) - "
                       f"Local: {entry['local_address']}, Remote: {entry['remote_address']} - "
                       f"Protocol: {entry['protocol']}, Status: {entry['status']}\n")

def run_logger(duration=60, interval=1):  # duration in seconds
    start_time = time.time()
    try:
        while time.time() - start_time < duration:
            log_entries = get_process_info()
            log_to_file(log_entries)
            print("Tick")
            time.sleep(interval)
    except KeyboardInterrupt:
        print("Logging stopped by user.")
    finally:
        print("Logging finished.")

# Run the logger with a 1-second interval and a total duration of 60 seconds
run_logger(60, 1)
