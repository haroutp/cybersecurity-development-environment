import socket

def scan_port(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(5)
    status = "closed"
    
    try:
        s.connect((ip, port))
        status = "open"
    except TimeoutError as e:
        status = "filtered"
    except ConnectionRefusedError as e:
        status = "closed"
    except OSError as e:
        status = "error"
    finally:
        s.close()
    
    return (port, status)

def scan_multiple_ports(ip, start_port, end_port):
    scanned_ports = []
    
    for port in range(start_port, end_port+1):
        scanned_ports.append(scan_port(ip, port))

    return scanned_ports

# result = scan_port("127.0.0.1", 8000)
# print(f"Port 8000: {result}")

result = scan_multiple_ports("127.0.0.1", 1, 450)
# print(result)

for port, status in result:
    if status == "open":
        print((port, status))