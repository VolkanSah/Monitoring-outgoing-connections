
# Monitoring Outgoing Connections 10/2024 - Version 2 - dev status

Join us in safeguarding our digital world, one connection at a time. This Python script actively monitors outgoing (TCP/UDP) connections, helping users stay alert to potential security threats, such as ransomware, spyware, or other suspicious network activities.

## Table of Contents

1. [Features & Improvements](#features--improvements)
2. [Log Format Examples](#log-format-examples)
3. [Requirements](#requirements)
4. [Configuration Options](#configuration-options)
5. [Additional Enhancements](#additional-enhancements)
6. [Why Monitor Outgoing Connections?](#why-monitor-outgoing-connections)
7. [Getting Started](#getting-started)
8. [License](#license)
9. [Thank You!](#thank-you)

## Features & Improvements

Version 2 introduces several enhancements that make the script more flexible, informative, and user-friendly:

### 1. Structured, Object-Oriented Code
   - Refactored to use Object-Oriented Programming (OOP) for easier maintenance, scalability, and customization.

### 2. Enhanced Logging Options
   - Generates separate log files with timestamps, providing clearer records for analysis.
   - Supports three log formats: `.txt`, `.csv`, and `.json`, offering flexibility for different analysis needs.
   - Logs include detailed and formatted entries to make data easy to read and process.

### 3. New Functionalities
   - **Protocol Detection**: Supports both TCP and UDP connections, expanding its monitoring scope.
   - **Process Path Information**: Logs the file path of the process that initiated each connection.
   - **Error Handling for Process Information**: Ensures the script continues functioning smoothly, even when encountering inaccessible process information.
   - **Configurable Batch Size and Logging Interval**: Allows customization of data collection intervals for optimal memory usage and logging efficiency.

### 4. Log Format
   - **TXT**: Organized entries with timestamps, protocols, and process details, making it easy to review logs quickly.
   - **CSV**: Structure facilitates data import and analysis with software like Excel or databases.
   - **JSON**: Suitable for structured data handling in applications or for further processing with automation tools.

---

## Log Format Examples

Logs are structured for readability and analysis. Here’s how they appear across formats:

---

- **TXT**: `[2024-10-26 14:30:45] TCP | Process: chrome (PID: 1234) | Local: 192.168.1.2:51234 | Remote: 8.8.8.8:443`
- **CSV**: `timestamp,protocol,process_name,process_path,pid,local_ip,local_port,remote_ip,remote_port,status`
- **JSON**: `{"timestamp": "2024-10-26 14:30:45", "protocol": "TCP", ...}`

---

## Requirements

- **Python 3.x**
- **psutil** library (Install via ---pip install psutil---)

Ensure you have the necessary permissions to access network and process data.

## Configuration Options

- **Log Directory**: Customize the directory where logs are saved (logs by default).
- **Batch Size and Interval**: Configure batch size and time intervals for logging in the monitor() method.

---

### Example Code Snippet

---

monitor = ConnectionMonitor(log_dir="custom_logs")  
monitor.monitor(interval=2, batch_size=100)

---

## Additional Enhancements

- **Graceful Shutdown**: The script is designed to handle `KeyboardInterrupt` smoothly, closing the monitoring session safely when needed.
- **Type Hints**: Improves code readability and quality, making it easier to understand and maintain.
- **Configurable Log Directory**: Logs can now be saved to custom directories, helping organize and separate network activity data.

## Why Monitor Outgoing Connections?

By monitoring outgoing network connections, you gain insight into potential threats within your system. This script provides all outgoing TCP and UDP connections, helping you identify any suspicious activities, which could be a first step in safeguarding your network against potential risks.

**Remember**: It’s essential to carefully analyze the logs and take appropriate action if suspicious connections are detected. This script serves as a preliminary tool for network security but is not a replacement for a comprehensive security solution.

## Getting Started

### Requirements
- Ensure the `psutil` library is installed (e.g., ---pip install psutil---).
- Run the script with appropriate permissions to access network and process information.

### Usage
The script runs indefinitely, continuously logging outgoing connections. You can stop the script using `CTRL+C` or the equivalent command for your environment.

### Customization
This script can be adjusted to meet specific requirements or integrated into larger security frameworks. We recommend consulting cybersecurity professionals for additional guidance.

## License

This project is copyright © by [VolkanSah](https://github.com/volkansah). 

## Thank You!

Your support is appreciated! If you find this project helpful, consider sharing it, giving a 🌟, or [becoming a sponsor](https://github.com/sponsors/volkansah). Follow for more updates and new projects!
