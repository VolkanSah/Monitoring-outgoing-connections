import psutil
import socket
import time
def monitor_outgoing_connections():
    while True:
        connections = psutil.net_connections(kind='tcp')
        for conn in connections:
            if conn.status == 'ESTABLISHED' and conn.raddr:
                remote_address = f"{conn.raddr[0]}:{conn.raddr[1]}"
                local_address = f"{conn.laddr[0]}:{conn.laddr[1]}"
                process_name = psutil.Process(conn.pid).name()

                # Log the outgoing connection
                log_message = f"Outgoing connection detected:\nProcess: {process_name}\nLocal Address: {local_address}\nRemote Address: {remote_address}\n"
                print(log_message)
                # You can write the log message to a file for further analysis

        time.sleep(1)

# Start monitoring outgoing connections
monitor_outgoing_connections()
