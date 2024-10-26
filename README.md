# Monitoring Outgoing  (TCP/UDP) -Connections v2.dev


This Python script is a handy tool to monitor outgoing network activity. It can be particularly useful in detecting potential security threats such as ransomware, spyware, or trojan activity.

## What does the script do?
The script continuously monitors all outgoing TCP connections from your system. For each established connection, it logs important information such as the name of the process that initiated the connection, and the local and remote addresses involved.

This logged information is not only printed on the console but is also stored in two file formats for ease of further analysis:

- A .txt file, where each connection is logged in a separate line.
- A .csv file, where each piece of information is separated by commas, making it easy to import and analyze in software like Excel.
The script saves the log files every five minutes to optimize memory usage.

## Why is this useful?
Monitoring outgoing connections can help you identify suspicious or unexpected network activity. While this script shows all outgoing TCP connections, not just those related to potential threats, it can aid in identifying connections that may warrant further investigation.

**It's crucial to analyze the logged information and take appropriate actions based on your findings. This script serves as a starting point for maintaining network security and mitigating potential risks.**

## Note
Please note that this script runs indefinitely. To stop the script, use CTRL+C or the equivalent command in your environment.

- Run the script with appropriate permissions and ensure that the required libraries (psutil) are installed!

- Please note that this script is a starting point and may need customization based on your specific requirements and environment. It's recommended to consult with cybersecurity professionals and consider integrating this monitoring mechanism into a comprehensive security solution.

## Thanks
**"Thank you! Your support is appreciated, and I would be grateful if you could share this project with others,  giving a :star: to my projects, or  
[becoming a 'Sponsor'](https://github.com/sponsors/volkansah). Don't forget to follow me for more free ideas and updates!"**

## Copyright
- Volkan (Sah) Kücükbudak
- [VolkanSah on Github](https://github.com/volkansah)
- [Developer Site](https://volkansah.github.io)

## License
This project is copyright by © [VolkanSah](https://github.com/volkansah) 

added:

 wichtigsten Änderungen:
```
Strukturierte Klasse:

Bessere Organisation des Codes durch OOP
Einfachere Wartung und Erweiterbarkeit


Verbesserte Logging:

Separate Log-Dateien mit Zeitstempel
Drei Formate: TXT, CSV und JSON
Strukturierte und leicht lesbare Log-Einträge


Neue Features:

Protokoll-Erkennung (TCP/UDP)
Prozess-Pfad-Information
Fehlerbehandlung für Prozessinformationen
Konfigurierbare Batch-Größe und Intervalle


Log-Format:

Zeitstempel zu Beginn jedes Eintrags
Klare Trennung der Informationen
Bessere Lesbarkeit durch formatierte Ausgabe


Zusätzliche Verbesserungen:

Typenhinweise für bessere Code-Qualität
Konfigurierbare Log-Verzeichnisse
Graceful Shutdown mit KeyboardInterrupt


```
Die Logs werden jetzt so formatiert:
```
TXT: [2024-10-26 14:30:45] TCP | Process: chrome (PID: 1234) | Local: 192.168.1.2:51234 | Remote: 8.8.8.8:443
CSV: timestamp,protocol,process_name,process_path,pid,local_ip,local_port,remote_ip,remote_port,status
JSON: {"timestamp": "2024-10-26 14:30:45", "protocol": "TCP", ...}
```
