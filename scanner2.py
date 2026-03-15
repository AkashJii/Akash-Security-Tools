import socket
from datetime import datetime

# Sirf IP maangega, port khud scan karega
ip = input("Target IP batao (e.g., 127.0.0.1): ")

print("-" * 50)
print(f"Scanning Target: {ip}")
print(f"Time Started: {datetime.now()}")
print("-" * 50)

try:
    # 1 se lekar 9000 tak saare ports scan karne ka loop
    for port in range(1, 9000):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.1) # Fast scanning ke liye
        
        # Connection test
        result = s.connect_ex((ip, port))
        if result == 0:
            print(f"[+] BOOM! Port {port} is OPEN!")
        s.close()

except KeyboardInterrupt:
    print("\nScan Cancelled by User.")
except socket.error:
    print("\nServer respond nahi kar raha.")

print("-" * 50)
print("Scan Complete! 😎")
