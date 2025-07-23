import platform
import subprocess
import ipaddress
import socket

def ping_host(ip):
    param = "-n" if platform.system().lower() == "windows" else "-c"
    command = ["ping", param, "1", str(ip)]
    result = subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return result.returncode == 0

def discover_hosts(network_input):
    print(f"\n🔍 Escaneando: {network_input}")
    ativos = []

    try:
        network = ipaddress.ip_network(network_input, strict=False)
        for ip in network.hosts():
            if ping_host(ip):
                ativos.append(str(ip))

    except ValueError:
        try:
            ip = socket.gethostbyname(network_input)
            print(f"🌐 {network_input} resolve para {ip}")
            if ping_host(ip):
                ativos.append(ip)
        except socket.gaierror:
            print("❌ Entrada inválida.")

    return ativos
