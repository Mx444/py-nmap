import nmap

scanner = nmap.PortScanner()

ip = input("❗ Enter the IP address you want to scan: ")
print(f"🔎 Scanning {ip} for open ports...")

scanner.scan(ip, arguments='-p-')

for host in scanner.all_hosts():
    print(f"🌐 Host: {host}")
    print(f"💻 Open ports: {list(scanner[host]['tcp'].keys())}")
