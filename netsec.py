import socket
import nmap
import time
import sys

def audit_network(host, ports):
    # Use the nmap library to perform a scan on the target host and specified ports
    nm = nmap.PortScanner()
    nm.scan(host, ports)

    # Check the status of each port and keep track of open ports
    open_ports = []
    for port in nm[host].all_tcp():
        if nm[host].tcp(port)['state'] == 'open':
            open_ports.append(port)
            print(f'🔓 Port {port} is open.')
        else:
            print(f'🔒 Port {port} is closed.')

    # Output a security assessment based on the open ports
    if len(open_ports) == 0:
        print('\n💪 Network is secure! No open ports were found.')
    elif len(open_ports) <= 3:
        print('\n💡 Network security is average. Some open ports were found.')
    else:
        print('\n🚨 Network is not secure! Several open ports were found.')

# Example usage with a scanning animation
def example_usage():
    host = '127.0.0.1'
    ports = '22-443'

    print(f'Scanning {host} on ports {ports}...\n')
    for i in range(5):
        sys.stdout.write('.')
        sys.stdout.flush()
        time.sleep(1)
    print('\n')
    
    audit_network(host, ports)

example_usage()
