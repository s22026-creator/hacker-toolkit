import socket
import requests
import sys

print(f"Python version: {sys.version}")
print(f"Socket module: OK")

response = requests.get("https://github.com")
print(f"requests module: OK (GitHub status: {response.status_code})")

ip = socket.gethostbyname("github.com")
print(f"GitHub IP: {ip}")
