import psutil
import socket
import time
def monitor_outgoing_connections():
    counter = 0
    log_messages = []
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
                # Add the log message to the list
                log_messages.append(log_message)
                counter += 1
                if counter >= 60:  # adjust this value as needed
                    # Write the log messages to a .txt file
                    with open("log.txt", "a") as txt_file:
                        txt_file.write('\n'.join(log_messages) + "\n")
                    # Write the log messages to a .csv file
                    with open("log.csv", "a") as csv_file:
                        csv_file.write(','.join(log_messages).replace('\n', ',') + "\n")
                    # Reset the counter and the list
                    counter = 0
                    log_messages = []
        time.sleep(1)
# Start monitoring outgoing connections
monitor_outgoing_connections()
