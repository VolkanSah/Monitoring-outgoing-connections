# Monitoring Outgoing (TCP/UDP) Connections v2.dev

This Python script is a robust tool designed to monitor outgoing network activity, specifically focusing on TCP and UDP connections. This can be particularly valuable for identifying potential security threats such as ransomware, spyware, or trojans by tracking outgoing network connections in real time.

## Features & Improvements

Version 2 has introduced several enhancements that make the script more flexible, informative, and user-friendly:

### 1. Structured, Object-Oriented Code
   - Refactored to use Object-Oriented Programming (OOP) for easier maintenance, scalability, and customization.

### 2. Enhanced Logging Options
   - The script generates separate log files with timestamps, providing clearer records for analysis.
   - Three log formats are supported: `.txt`, `.csv`, and `.json`, offering flexibility for different analysis needs.
   - Logs include detailed and formatted entries to make the data easy to read and process.

### 3. New Functionalities
   - **Protocol Detection**: Supports both TCP and UDP connections, expanding its monitoring scope.
   - **Process Path Information**: Logs the file path of the process that initiated each connection.
   - **Error Handling for Process Information**: Ensures that the script continues to function smoothly, even when encountering inaccessible process information.
   - **Configurable Batch Size and Logging Interval**: Allows customization of data collection intervals for optimal memory usage and logging efficiency.

### 4. Log Format
   - **TXT**: Organized entries with timestamps, protocols, and process details, making it easy to review logs quickly.
   - **CSV**: Structure facilitates data import and analysis with software like Excel or databases.
   - **JSON**: Suitable for structured data handling in applications or for further processing with automation tools.

Examples:
```
TXT: [2024-10-26 14:30:45] TCP | Process: chrome (PID: 1234) | Local: 192.168.1.2:51234 | Remote: 8.8.8.8:443
CSV: timestamp,protocol,process_name,process_path,pid,local_ip,local_port,remote_ip,remote_port,status
JSON: {"timestamp": "2024-10-26 14:30:45", "protocol": "TCP", ...}
```


### 5. Additional Enhancements
- **Graceful Shutdown**: The script is designed to handle `KeyboardInterrupt` smoothly, closing the monitoring session safely when needed.
- **Type Hints**: Improves code readability and quality, making it easier to understand and maintain.
- **Configurable Log Directory**: Logs can now be saved to custom directories, helping organize and separate network activity data.

## Why Monitor Outgoing Connections?
By monitoring outgoing network connections, you gain insight into potential threats within your system. This script provides all outgoing TCP and UDP connections, helping you identify any suspicious activities, which could be a first step in safeguarding your network against potential risks.

**Remember**: It’s essential to carefully analyze the logs and take appropriate action if suspicious connections are detected. This script serves as a preliminary tool for network security but is not a replacement for a comprehensive security solution.

## Getting Started

### Requirements
- Ensure the `psutil` library is installed (e.g., `pip install psutil`).
- Run the script with appropriate permissions to access network and process information.

### Usage
The script runs indefinitely, continuously logging outgoing connections. You can stop the script using `CTRL+C` or the equivalent command for your environment.

### Customization
This script can be adjusted to meet specific requirements or integrated into larger security frameworks. We recommend consulting cybersecurity professionals for additional guidance.

## License
This project is copyright © [VolkanSah](https://github.com/volkansah)

## Thank You!
Your support is appreciated! If you find this project helpful, consider sharing it, giving a 🌟, or [becoming a sponsor](https://github.com/sponsors/volkansah). Follow for more updates and new projects!
