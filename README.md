# Network Process Logger README

## Overview
This Python script is designed for logging network-related process information on a system. It gathers details about processes involved in network connections, including their names, IDs, local and remote addresses, protocols used, and connection statuses. This data is periodically logged to a file for analysis or monitoring purposes.

## Features
- **Process Information Retrieval**: Extracts detailed information about each process involved in internet connections (TCP/UDP).
- **Continuous Logging**: Logs information at regular intervals for a specified duration.
- **Customizable Logging Intervals and Duration**: Users can define how long the logger runs and the frequency of logging.
- **Robust Process Handling**: Gracefully handles scenarios where a process is terminated or inaccessible during logging.
- **File Output**: Logs are written to a text file for easy storage and review.

## Dependencies
- `psutil`: This package is used for accessing system details and process information.
- `datetime`: For timestamping log entries.
- `socket`: To determine the type of network connection (TCP/UDP).
- `time`: For managing the logging intervals and duration.

## How to Use
1. **Install Dependencies**: Ensure that `psutil` is installed in your Python environment. It can be installed via pip:
   ```
   pip install psutil
   ```
2. **Running the Script**: Simply execute the script to start logging. By default, it logs every 1 second for a total duration of 60 seconds.
3. **Customizing Logging Parameters**: You can modify the `run_logger` function call at the end of the script to change the logging duration and interval. For example, `run_logger(120, 2)` will log for 120 seconds at 2-second intervals.

## Function Descriptions
- `get_process_info()`: Gathers network connection details of all processes.
- `log_to_file(entries, filename="network_log.txt")`: Logs the gathered information to a specified file.
- `run_logger(duration=60, interval=1)`: Controls the overall logging operation, defining how long and how frequently logging occurs.

## Output Format
The script outputs logs in the following format:
```
[Timestamp] - [Process Name] ([Process ID]) - Local: [Local Address], Remote: [Remote Address] - Protocol: [TCP/UDP], Status: [Connection Status]
```

## Limitations
- **Platform Dependency**: The script's behavior might vary depending on the operating system due to differences in how process information is managed.
- **Permission Requirements**: Some process details may require elevated permissions to access.

## License
This script is released under the MIT License. 
