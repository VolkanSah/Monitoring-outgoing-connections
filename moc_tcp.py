# Monitoring outgoing connections 10/2024 Version 2
# Join us in safeguarding our digital world - one connection at a time. For more insights and understanding, 
# visit https://github.com/VolkanSah/Monitoring-outgoing-connections. 
# Your support fuels a safer, more secure online experience for all.
import psutil
import socket
import time
from datetime import datetime
import csv
import os
import json
from typing import Dict, List, Optional

class ConnectionMonitor:
    def __init__(self, log_dir: str = "logs"):
        """Initialisiert den Connection Monitor mit konfigurierbarem Log-Verzeichnis."""
        self.log_dir = log_dir
        self.counter = 0
        self.connections_cache: Dict[str, dict] = {}
        self.setup_log_directory()

    def setup_log_directory(self) -> None:
        """Erstellt das Log-Verzeichnis falls es nicht existiert."""
        if not os.path.exists(self.log_dir):
            os.makedirs(self.log_dir)

    def get_timestamp(self) -> str:
        """Generiert einen formatierten Zeitstempel."""
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def get_protocol_info(self, connection) -> str:
        """Ermittelt das verwendete Protokoll."""
        return connection.type if hasattr(connection, 'type') else 'UNKNOWN'

    def get_process_info(self, pid: int) -> tuple:
        """Ermittelt Prozessinformationen sicher."""
        try:
            process = psutil.Process(pid)
            return process.name(), process.exe()
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            return "Unknown", "Unknown"

    def format_connection_info(self, connection) -> Optional[dict]:
        """Formatiert die Verbindungsinformationen in ein strukturiertes Dictionary."""
        if not (connection.status == 'ESTABLISHED' and connection.raddr):
            return None

        timestamp = self.get_timestamp()
        process_name, process_path = self.get_process_info(connection.pid)
        protocol = self.get_protocol_info(connection)
        
        return {
            'timestamp': timestamp,
            'protocol': protocol,
            'process_name': process_name,
            'process_path': process_path,
            'pid': connection.pid,
            'local_ip': connection.laddr[0],
            'local_port': connection.laddr[1],
            'remote_ip': connection.raddr[0],
            'remote_port': connection.raddr[1],
            'status': connection.status
        }

    def write_logs(self, connections: List[dict]) -> None:
        """Schreibt die Verbindungsinformationen in verschiedene Log-Formate."""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        # TXT Log
        txt_path = os.path.join(self.log_dir, f"connections_{timestamp}.txt")
        with open(txt_path, "a", encoding='utf-8') as txt_file:
            for conn in connections:
                txt_file.write(
                    f"[{conn['timestamp']}] {conn['protocol']} | "
                    f"Process: {conn['process_name']} (PID: {conn['pid']}) | "
                    f"Local: {conn['local_ip']}:{conn['local_port']} | "
                    f"Remote: {conn['remote_ip']}:{conn['remote_port']}\n"
                )

        # CSV Log
        csv_path = os.path.join(self.log_dir, f"connections_{timestamp}.csv")
        with open(csv_path, "a", newline='', encoding='utf-8') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=connections[0].keys())
            if os.path.getsize(csv_path) == 0:
                writer.writeheader()
            writer.writerows(connections)

        # JSON Log
        json_path = os.path.join(self.log_dir, f"connections_{timestamp}.json")
        with open(json_path, "a", encoding='utf-8') as json_file:
            for conn in connections:
                json.dump(conn, json_file)
                json_file.write('\n')

    def monitor(self, interval: int = 1, batch_size: int = 60):
        """Hauptfunktion zum Monitoring der Verbindungen."""
        print(f"Starting connection monitoring... Logs will be saved to {self.log_dir}")
        connections_batch = []

        try:
            while True:
                current_connections = psutil.net_connections(kind='inet')  # Überwacht TCP und UDP
                
                for conn in current_connections:
                    conn_info = self.format_connection_info(conn)
                    if conn_info:
                        connections_batch.append(conn_info)
                        print(f"[{conn_info['timestamp']}] New connection detected: "
                              f"{conn_info['process_name']} -> {conn_info['remote_ip']}:{conn_info['remote_port']}")
                
                if len(connections_batch) >= batch_size:
                    self.write_logs(connections_batch)
                    connections_batch = []

                time.sleep(interval)

        except KeyboardInterrupt:
            print("\nMonitoring stopped by user.")
            if connections_batch:
                self.write_logs(connections_batch)

def main():
    monitor = ConnectionMonitor()
    monitor.monitor(interval=1, batch_size=60)

if __name__ == "__main__":
    main()
